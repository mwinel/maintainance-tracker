from passlib.hash import pbkdf2_sha256

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
			'password': u'lava12'
		}
	]

	def __init__(self, id, username, email, password):
		""" Initialize user objects. """
		self.id = id,
		self.username = username,
		self.email = email,
		self.password = password

	@staticmethod
	# Generate a hashed string to be
	# stored by our class model.
	def generate_hash(password):
		return pbkdf2_sha256.encrypt(password, rounds = 20000, salt_size = 16)

	@staticmethod
	# Check a given password.
	def verify_hash(password, hash):
		return pbkdf2_sha256.verify(password, hash)

	def getUsers():
		""" Method to return a list of users. """
		return User.users, 200

	def getUser(id):
		""" Method to return user by id. """
		user = [user for user in User.users if user['id'] == id]
		if not user:
			return {'message': 'User not found'}
		return {'user': user[0]}, 200

	def get_user_by_username(self, username):
		""" Method to return user by username. """
		user = [x for x in User.users if x.get("username") == username]
		if user:
			return user[0]
		return None

class RevokedToken:
	""" This class provides a way to store revoked token data. """

	tokens = []

    # Strore the token id and its unique identifier.
	def __init__(id, jti):
		self.id = id,
		self.jti = jti

	@classmethod
	def is_jti_blacklisted(cls, jti):
		""" Method to check if token is revoked. """
		token = [x for x in tokens if x.get("jti") == jti]
		return bool(token)

class Request:
	""" This class provides a way to store requests data. """

	requests = [
		{
			'id': 1,
			'title': u'request 1',
			'description': u'Track maintainance'
		},
		{
			'id': 2,
			'title': u'request 2',
			'description': u'Track repairs'
		}
	]

	def __init__(self, id, title, description):
		""" Initialize request objects. """
		self.id = id,
		self.title = title,
		self.description = description
