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
		for user in User.users:
			if password == User.verify_hash(data['password'], hash):
				# access_token = create_access_token(identity = data['username'])
				# refresh_token = create_refresh_token(identity = data['username'])
				return {
					'message': 'Logged in as {}'.format(data['username']),
					# 'access token': access_token.decode('utf-8'),
					# 'refresh token': refresh_token.decode('utf-8')
				}, 200
		return {
			'message': 'Something went wrong'
		}, 500

class UserLogoutAccess(Resource):
	def post(self):
		return {'message': 'User logout'}

class UserLogoutRefresh(Resource):
	# Call the method to access token to logout.
	def post(self):
		return {'message': 'User logout'}

class TokenRefresh(Resource):
	# Call the method to refresh token to logout.
	def post(self):
		return {'message': 'Refresh token'}

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
