import sys, re
from typing import Dict, Optional, List, Any
import torch
from torch import nn
import numpy as np
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModel, BertForSequenceClassification, BertModel, BertPreTrainedModel
# from metrics import CategoricalAccuracy, F1Measure

class BertTextClassifier(nn.Module):

	def __init__(self,
              bert_model: str,
              num_labels: int,
              dropout: float=0.2,
              freeze_model: bool = True,
              verbose_metrics: bool = False,
              pbar_width=0.1,
              params_to_freeze:  Optional[List[str]] = None):
		super().__init__()

		self.pbar_width = pbar_width


		#if finetune:
		#self.bert = AutoModel.from_pretrained(bert_model)
		self.bert = BertModel.from_pretrained(bert_model)
		if freeze_model:
			if params_to_freeze is not None:
				for name, param in self.bert.named_parameters():
					if any([re.match(pattern, name) for pattern in params_to_freeze]):
						param.requires_grad = False
			else:
				for name, param in self.named_parameters():
					param.requires_grad = False
		self.dropout = torch.nn.Dropout(dropout)
		self.num_classes = num_labels
		self.classifier_feedforward = torch.nn.Linear(self.bert.config.hidden_size  , self.num_classes)

		# self.labels = labels

	def forward(self, batch, evaluation=False, cls=True):
		"""
		Parameters
		----------
		"""
		input_ids, input_mask, segment_ids, label_ids = batch
		embeddings = self.bert(input_ids = input_ids, token_type_ids = segment_ids, attention_mask = input_mask)
		pooled = self.dropout(embeddings[0][:, 0, :])

		#pooled = self.dropout(embedded_text)
		logits = self.classifier_feedforward(pooled)
		return logits, label_ids.float()

	def is_cuda(self):
		''' Check if the model is stored on the GPU. '''
		return next(self.parameters()).is_cuda

