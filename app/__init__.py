from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from config import app_config


jwt = JWTManager()

def create_app(config_class):
	app = Flask(__name__)
	app.config.from_object(app_config[config_class])
	app.config['JWT_SECRET_KEY'] = "jwt-secret-string"
	api = Api(app)
	jwt = JWTManager(app)

	return app

app = create_app("development")
api = Api(app = app, prefix = "/api/v1")
