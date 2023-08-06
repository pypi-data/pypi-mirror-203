import json
from flask import jsonify, request, Response
from flask_restful import Resource
from sarcat.models.legacy.modules import load_model


class Classification(Resource):

	def __init__(self, model_name="data/model_64.96.pt"):
		self.model, chekpoints = load_model(model_name)


	def get(self):

		inputs = request.get_json()

		if 'title' in inputs and 'abstract' in inputs:

			title = inputs['title']
			abstract = inputs['abstract']

			try:
				preds = self.model.predict(title, abstract)
				print(preds)
				data = json.dumps(preds)
				response = Response(data, mimetype='application/json')
				response.status_code = 200
			except Exception as error:
				print(error)
				response = jsonify({"message": str(error)})
				response.status_code = 500
		else:
			esponse = jsonify({"message": str("Api needs title and abstract as inputs")})
			response.status_code = 500
		return response




