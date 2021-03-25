import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True

    SQLALCHEMY_ECHO = True

    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    TESTING = True

    SQLALCHEMY_ECHO = True

    SESSION_COOKIE_SECURE = False
