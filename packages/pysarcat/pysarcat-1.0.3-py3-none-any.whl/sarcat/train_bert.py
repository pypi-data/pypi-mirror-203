import time
from data.dataset import from_tsv, get_data
from data.dataloader import AbsLoader
import argparse, sys, os, random, torch, dill
from torch import optim
from torch.nn import functional as F
import wandb
from tqdm.auto import tqdm
from sklearn.metrics import classification_report
import warnings, sys
from sklearn.metrics import f1_score
from options import train_opts, model_opts
from data.utils import get_cats, BatchWrapper, get_mcat_dict, get_class_weights, get_class_weights2, get_mcat_masks, cats2mcats
from transformers import AutoTokenizer,BertTokenizer
from models.bert2 import BertTextClassifier
from losses import NestedBCELoss


def main(args):

    device = torch.device('cuda' if args.gpu  else 'cpu')

    output= args.output
    if not os.path.isdir(output):
        os.mkdir(output)

    # Set up the columns in the tsv file with their associated fields
    cats = get_cats(args.category_dir)
    mcats_dict = get_mcat_dict(args.category_dir)
    if cats is None:
        sys.exit(f"{args.category} does not eexist.")
    cats = cats['id']


    df_dataset = from_tsv(args.train)
    train, val = get_data(df_dataset, cats)

    _dataloader = AbsLoader()

    tokenizer = BertTokenizer.from_pretrained(
                    args.model_name,
                    do_lower_case=True,
                    # cache_dir=model_args.cache_dir,
                    use_fast=True,
                    revision='main',
                    use_auth_token=None,
                    local_files_only=True)
    train_dl = _dataloader.iterator(train,
                            tokenizer,
                            max_seq_length=args.max_seq_length,
                            set_type='train',
                            batch_size=args.batch_size,
                            output=output,
                            save_dataset=args.save_dataset,
                            load_dataset=args.load_dataset)
    valid_dl = _dataloader.iterator(train,
                            tokenizer,
                            max_seq_length=args.max_seq_length,
                            set_type='valid',
                            batch_size=args.batch_size,
                            output=output,
                            save_dataset=args.save_dataset,
                            load_dataset=args.load_dataset)

    model = BertTextClassifier(bert_model=args.model_name,
                               num_labels=_dataloader.num_classes,
                               pbar_width=args.pbar_width).to(device)



    # Sign into wandb and log metrics from model
    if args.use_wandb:
        config = {
            'name': args.wandb_name,
            'mcat_ratio': args.mcat_ratio,
            'epochs': args.epochs,
            'lr': args.lr,
            'batch_size': train_dl.batch_size,
            'ema': args.ema,
            'model_name': args.model_name,
            'max_seq_length': args.max_seq_length,
            'num_classes': model.num_classes
        }
        wandb.init(project = 'article_classification', config = config)
        wandb.watch(model)

    weights = get_class_weights2(train_dl, pbar_width = model.pbar_width,
        cats = cats, mcats_dict = mcats_dict, batch_size=args.batch_size, device=device)

    criterion = NestedBCELoss(**weights, mcat_ratio = 0.1,
        cats = cats, mcats_dict = mcats_dict, device=device)
    optimizer = optim.Adam(model.parameters(), lr = args.lr)
    mcat_masks = get_mcat_masks(cats, mcats_dict, device)

    start_epoch = 0
    scaler = torch.cuda.amp.GradScaler()

    if args.resume:
        checkpoint = torch.load(args.resume_from_path, map_location = lambda storage, log: storage)
        model.load_state_dict(checkpoint['state_dict'])
        if 'optimizer' in checkpoint:
            optimizer.load_state_dict(checkpoint['optimizer'])
        if 'epoch' in checkpoint:
            start_epoch = checkpoint['epoch']

    if model.is_cuda():
        mcat_masks = mcat_masks.to(device)
        criterion = criterion.to(device)
    avg_loss, avg_cat_f1, avg_mcat_f1, best_score = 0, 0, 0, 0
    overwrite_model = False

    for epoch in range(start_epoch, args.epochs):

        with tqdm(total = len(train_dl) * train_dl.batch_size,
            ncols = args.pbar_width) as pbar:
            model.train()
            for idx, batch in enumerate(train_dl):
                start_time = time.time()
                optimizer.zero_grad(set_to_none=True)
                batch = tuple(t.to(device) for t in batch)
                with torch.cuda.amp.autocast():
                    y_hat, y_train = model(batch)
                y_train = y_train.squeeze()
                preds = torch.sigmoid(y_hat)

                # Get master cat predictions
                my_hat, my_train = cats2mcats(y_hat, y_train,
                    masks = mcat_masks, cats = cats, mcats_dict = mcats_dict, device=device)
                mpreds = torch.sigmoid(my_hat)


                # Calculate loss and perform backprop
                loss = criterion(y_hat, y_train)
                # loss.backward()
                scaler.scale(loss).backward()
                # optimizer.step()
                scaler.step(optimizer)

                # Compute f1 scores
                with warnings.catch_warnings():
                    warnings.simplefilter('ignore')
                    cat_f1 = f1_score(preds.cpu() > 0.5, y_train.cpu(),
                        average = 'samples')
                    mcat_f1 = f1_score(mpreds.cpu() > 0.5, my_train.cpu(),
                        average = 'samples')

                # Keep track of the current iteration index
                iteration = epoch * len(train_dl) * train_dl.batch_size
                iteration += idx * train_dl.batch_size

                # Exponentially moving average of loss and f1 scores
                avg_loss = args.ema * avg_loss + (1 - args.ema) * float(loss.item())
                avg_loss /= 1 - args.ema ** (iteration / (1 - args.ema) + 1)
                avg_cat_f1 = args.ema * avg_cat_f1 + (1 - args.ema) * float(cat_f1)
                avg_cat_f1 /= 1 - args.ema ** (iteration / (1 - args.ema) + 1)
                avg_mcat_f1 = args.ema * avg_mcat_f1 + (1 - args.ema) * float(mcat_f1)
                avg_mcat_f1 /= 1 - args.ema ** (iteration / (1 - args.ema) + 1)

                scaler.update()

            # Compute validation scores
            with torch.no_grad():
                model.eval()

                val_loss, val_cat_f1, val_mcat_f1 = 0, 0, 0
                y_vals, y_hats = [], []
                for idx, batch in enumerate(valid_dl):

                    batch = tuple(t.to(device) for t in batch)

                    y_hat, y_val = model(batch)
                    y_val = y_val.squeeze()
                    preds = torch.sigmoid(y_hat)

                    # Get mcat predictions
                    my_hat, my_val = cats2mcats(y_hat, y_val,
                        masks = mcat_masks, cats = cats, mcats_dict = mcats_dict, device=device)
                    mpreds = torch.sigmoid(my_hat)

                    # Collect the true and predicted labels
                    y_vals.append(y_val)
                    y_hats.append(preds > 0.5)

                    # Accumulate loss
                    _loss = criterion(y_hat,y_val, weighted = False)
                    val_loss += float(_loss.item())

                    # Accumulate f1 scores
                    with warnings.catch_warnings():
                        warnings.simplefilter('ignore')
                        val_cat_f1 += f1_score(preds.cpu() > 0.5, y_val.cpu(),
                            average = 'samples')
                        val_mcat_f1 += f1_score(mpreds.cpu() > 0.5,
                            my_val.cpu(), average = 'samples')

                # Concatenate the true and predicted labels
                y_val = torch.cat(y_vals, dim = 0)
                y_hat = torch.cat(y_hats, dim = 0)

                # Compute the average loss and f1 scores
                val_loss /= len(valid_dl)
                val_cat_f1 /= len(valid_dl)
                val_mcat_f1 /= len(valid_dl)

                # Log wandb
                if args.use_wandb:
                    wandb.log({
                        'val loss': val_loss,
                        'val cat f1': val_cat_f1,
                        'val mcat f1': val_mcat_f1
                    })

                # If the current cat f1 score is the best so far, then
                # replace the stored model with the current one


                with warnings.catch_warnings():

                    warnings.simplefilter('ignore')
                    scores = classification_report(
                        y_true = y_val.cpu(),
                        y_pred = y_hat.cpu(),
                        target_names = cats,
                        output_dict = True
                    )
                    data = {
                        'epoch': epoch,
                        'params': args,
                        'state_dict': model.state_dict(),
                        'optimizer': optimizer.state_dict(),
                        'scores': scores
                    }
                torch.save(data, f'{output}/checkpoint_last.pt')

                if val_cat_f1 > best_score:
                    model_fname = os.path.join(output, f'model_{val_cat_f1 * 100:.2f}.pt')
                    best_score = val_cat_f1


                    if overwrite_model:
                        for f in get_path(model.data_dir).glob(f'model*.pt'):
                            f.unlink()

                    with warnings.catch_warnings():
                        warnings.simplefilter('ignore')
    #                         path = get_path(model.data_dir) / model_fname
                        torch.save(data, model_fname)

                # Update progress bar
                desc = f'Epoch {epoch:2d} - '\
                       f'loss {avg_loss:.4f} - '\
                       f'cat f1 {avg_cat_f1:.4f} - '\
                       f'mcat f1 {avg_mcat_f1:.4f} - '\
                       f'val_loss {val_loss:.4f} - '\
                       f'val cat f1 {val_cat_f1:.4f} - '\
                       f'val mcat f1 {val_mcat_f1:.4f}'
                pbar.set_description(desc)






if __name__ == "__main__":
    parser = argparse.ArgumentParser('')

    train_opts(parser)
    model_opts(parser)
    args = parser.parse_args()

    os.environ['CUDA_VISIBLE_DEVICES'] = str(args.gpu_id)
    main(args)
