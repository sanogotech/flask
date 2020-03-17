import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI ="sqlite:///posts.db"
    SECRET_KEY = (os.environ.get('SECRET_KEY') or 
        'asrtarstaursdlarsn')

class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    CSRF_ENABLED = True
    # If you do that, your browser will not cache static assets that are served by Flask
    #No Cache Browser
    SEND_FILE_MAX_AGE_DEFAULT =0
    SECRET_KEY = (os.environ.get('SECRET_KEY') or 
    'this-really-needs-to-be-changed')


class TestingConfig(Config):
    TESTING = True