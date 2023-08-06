import os
from flask import Flask
from flask_restful import Api
from sarcat.api.classification import Classification

app = Flask(__name__)
api = Api(app)


if __name__ == "__main__":
    host = os.getenv('API_HOST', '0.0.0.0')
    port = os.getenv('API_PORT', 5000)

    api.add_resource(Classification, '/api/v1/resources/categorization/')


    app.run(host='0.0.0.0', port=port, debug=True, use_reloader=True)