import os
import dotenv

dotenv.load_dotenv()

DEBUG = False
TESTING = False

ENV = os.environ.get('ENV', 'dev').lower()

if ENV in ['dev', 'development']:
    DEBUG = True

if ENV in ['qa', 'test', 'testing']:
    TESTING = True

SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', 'false').lower() == 'true'

LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL', 'DEBUG')
LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'detailed': {
            'class': 'logging.Formatter',
            'format': '%(asctime)s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': LOGGING_LEVEL,
            'formatter': 'detailed',
        }
    },
    'loggers': {},
    'root': {
        'level': LOGGING_LEVEL,
        'handlers': ['console']
    },
}