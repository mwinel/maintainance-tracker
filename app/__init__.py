from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from config import app_config


jwt = JWTManager()

def create_app(config_class):
	app = Flask(__name__)
	app.config.from_object(app_config[config_class])
	app.config['JWT_SECRET_KEY'] = "tPXJY3X37Qybz4QykV+hOyUxVQeEXf1Ao2C8upz+fGQXKsM"
	app.config['JWT_BLACKLIST_ENABLED'] = True
	app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
	api = Api(app)
	jwt = JWTManager(app)

	# Callback everytime a secured endpoint is accessed.
	# Return True if token is blacklisted.
	# Return False if token is not blacklisted.
	@jwt.token_in_blacklist_loader
	def check_if_token_in_blacklist(decrypted_token):
		jti = decrypted_token['jti']
		return models.RevokedToken.is_jti_blacklisted(jti)

	return app

app = create_app("development")
api = Api(app = app, prefix = "/api/v1")
