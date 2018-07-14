# Create classes to store data.

class User:
	""" This class provides a way to store user data. """

	users = [
		{
			'id': 1,
			'username': u'mwinel',
			'email': u'mwinel@example.com',
			'password': u'code618'
		},
		{
			'id': 2,
			'username': u'lucy',
			'email': u'lucy@example.com',
			'password': u'123456'
		}
	]

	def __init__(self, id, username, email, password):
		""" Initialize objects. """
		self.id = user_id,
		self.username = username,
		self.email = email,
		self.password = password

	def getUsers():
		""" Method to return a list of users. """
		return User.users, 200

	def getUser(id):
		user = [user for user in User.users if user['id'] == id]
		if not user:
			return {'message': 'User not found'}
		return {'user': user[0]}, 200
