import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False

    SECRET_KEY = 'changemebitch'
    #SERVER_NAME = 'changeme.bitch'

    SITE_NAME = 'skeletyon'

    #Uncomment for SQLite or use MySQL
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'application/data.sqlite')
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql:username:password@localhost/db_name'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    SESSION_COOKIE_SECURE = True

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
