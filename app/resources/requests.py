from flask_restful import Resource
from app import create_app

class CreateRequest(Resource):
	# Call method to create request.
	def post(self):
		return {'message': 'Create request'}

class UpdateRequest(Resource):
	# Call method to update request.
	def put(self):
		return {'message': 'Update request'}

class GetRequest(Resource):
	# Call method to return a single request.
	def get(self):
		return {'message': 'Return one request'}

class GetRequests(Resource):
	# Call method to return all requests.
	def get(self):
		return {'message': 'Return a list of requests'}

class DeleteRequest(Resource):
	# Call method to delete a request.
	def post(self):
		return {'message': 'Delete a request'}
