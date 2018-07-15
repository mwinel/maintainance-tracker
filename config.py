import os 


class Config(object):
	""" Default configurations. """
	
	DEBUG = False
	TESTING = False

class DevelopmentConfig(Config):
	""" Development configurations. """

	DEBUG = True
	TESTING = True

class TestingConfig(Config):
	""" Test configurations. """

	DEBUG = True
	TESTING = True

class ProductionConfig(Config):
	""" Production configurations. """

	DEBUG = False
	TESTING = False

app_config = {
	"development": DevelopmentConfig,
	"testing": TestingConfig,
	"production": ProductionConfig
}



