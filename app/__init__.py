from flask import Flask
from flask_restful import Api


def create_app(config_class):
	app = Flask(__name__)
	api = Api(app)

	return app

app = create_app("development")
api = Api(app = app, prefix = "/api/v1")
