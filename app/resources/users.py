from passlib.hash import pbkdf2_sha256
from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token, 
	create_refresh_token, jwt_required, jwt_refresh_token_required, 
	get_jwt_identity, get_raw_jwt)
from app import create_app
from app.models import User

class UserRegistration(Resource):
	# Call the method to create or register a user.
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('username', required = True)
		parser.add_argument('email', required = True)
		parser.add_argument('password', required = True)
		
		data = parser.parse_args()
		username = data['username']
		email = data['email']

		# Check if user exists.
		for user in User.users:
			if username == user['username']:
				return {
					'message': 'User {} already exists'.format(data['username'])
				}, 400
			if email == user['email']:
				return {
					'message': 'User with {} already exists'.format(data['email'])
				}, 400

		user = {
			"id": User.users[-1]['id'] + 1,
			"username": data["username"],
			"email": data["email"],
			"password": User.generate_hash(data["password"])
		}
		User.users.append(user)
		access_token = create_access_token(identity = data['username'])
		refresh_token = create_refresh_token(identity = data['username'])
		return {
			'message': 'User successfully created',
			'access token': access_token,
			'refresh token': refresh_token
		}, 201

class UserLogin(Resource):
	# Call the method to login a user.
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('username', required = True)
		parser.add_argument('password', required = True)

		data = parser.parse_args()
		username = data['username']
		password = data['password']

		current_user = User.get_user_by_username(data['username'], username)
		if not current_user:
			return {
				'message': 'User {} doesn\'t exist'.format(data['username'])
			}

		if pbkdf2_sha256.verify(password, pbkdf2_sha256.hash(password)):
			access_token = create_access_token(identity = data['username'])
			refresh_token = create_refresh_token(identity = data['username'])
			return {
				'message': 'Logged in as {}'.format(data['username']),
				'access token': access_token,
				'refresh token': refresh_token
			}

class UserLogoutAccess(Resource):
	@jwt_required
	def post(self):
		jti = get_raw_jwt()['jti']
		try:
			revoked_token = RevokedToken(jti = jti)

class UserLogoutRefresh(Resource):
	# Call the method to access token to logout.
	def post(self):
		return {'message': 'User logout'}

class TokenRefresh(Resource):
	# Call the method to reissue a refresh token.
	# You can only access this path using a refresh token.
	@jwt_refresh_token_required
	def post(self):
		# Identify user by extracting identity from refresh token.
		current_user = get_jwt_identity()
		# Use identity to return new access token 
		# and return it to the user.
		access_token = create_access_token(identity = current_user)
		return {
		    'access_token': access_token
		}

class GetUsers(Resource):
	# Call method to return all users.
	def get(self):
		return User.getUsers()

class GetUser(Resource):
	# Call method to return all users.
	def get(self, id):
		return User.getUser(id)

class SecretResource(Resource):
	@jwt_required
	def get(self):
		return {
			'message': 618
		}
