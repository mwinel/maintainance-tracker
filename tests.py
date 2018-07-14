import json
import unittest
from flask_testing import TestCase
from app import create_app
from run import app
from config import app_config

app.config.from_object(app_config["testing"])

class TestBase(TestCase):
	""" Base configurations for the tests. """

	def create_app(self):
		""" Returns app. """
		return app

	def setUp(self):
		""" Create test database and set up test client. """
		self.app = app.test_client()

	def test_index(self):
		""" Test response to the index endpoint. """
		response = self.app.get('/api/v1/')
		self.assertEqual(response.status_code, 200)
		output = json.loads(response.data)
		self.assertEqual(output, {'message': 'Maintainance Tracker.'})

if __name__ == "__main__":
	unittest.main()
