from flask_restful import Resource
from app import create_app

class Index(Resource):
    # Call the method to Get the index response.
    def get(self):
        """ Return a welcome message. """
        return {"message": "Maintainance Tracker."}
