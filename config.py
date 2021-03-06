"""Main configuration file"""
# Define the application directory
from os import getenv, path
from environs import Env

BASE_DIR = path.abspath(path.dirname(__file__))
env = Env()

current_env = getenv("FLASK_ENV") or 'local'
if not path.exists("{}.env".format(current_env)):
    raise EnvironmentError("FLASK_ENV not set properly for {} env.".format(
        current_env))

# loading the selected .env file
project_folder = path.expanduser(BASE_DIR)
env.read_env(path.join(project_folder, "{}.env".format(current_env)))


# ######################## #
# #### Configurations #### #
# ######################## #


DEBUG = env('DEBUG')

SQLALCHEMY_DATABASE_URI = env('SQLALCHEMY_DATABASE_URI')
# To disable tracking modifications on Objects by Flask-SQLAlchemy
SQLALCHEMY_TRACK_MODIFICATIONS = env('SQLALCHEMY_TRACK_MODIFICATIONS')
# MongoDB Configuration
MONGODB_DATABASE_URI = env("MONGODB_DATABASE_URI")
MAX_POOL_SIZE = env.int("MAX_POOL_SIZE")
MIN_POOL_SIZE = env.int("MIN_POOL_SIZE")
MAX_IDLE_TIME = env.int("MAX_IDLE_TIME")
CONNECTION_TIMEOUT = env.int("CONNECTION_TIMEOUT")
HEARTBEAT_FREQUENCY = env.int("HEARTBEAT_FREQUENCY")
SERVER_SELECTION_TIMEOUT = env.int("SERVER_SELECTION_TIMEOUT")

# Redis Configuration
REDIS_URL = getenv("REDIS_URL")

DATABASE_CONNECT_OPTIONS = env('DATABASE_CONNECT_OPTIONS')

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = env.int('THREADS_PER_PAGE')

# Enable protection again *Cr-site Request Forgery (CSRF)*
CSRF_ENABLED = env.bool('CSRF_ENABLED')

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = env('CSRF_SESSION_KEY')

# Secret key for signing cookies
SECRET_KEY = env('SECRET_KEY')

AUTH_TOKEN_TTL_MINUTES = env.int('AUTH_TOKEN_TTL_MINUTES')
JWT_SECRET_KEY = env('JWT_SECRET_KEY')

HOOKS_REQUIRED = env.bool('HOOKS_REQUIRED')

# Logs
LOG_LEVEL = env('LOG_LEVEL')
LOG_FILE_PATH = env('LOG_FILE_PATH')

# email
MAIL_SERVER = env('MAIL_SERVER')
MAIL_USERNAME = env('MAIL_USERNAME')
MAIL_PASSWORD = env('MAIL_PASSWORD')
MAIL_DEFAULT_SENDER = env('MAIL_DEFAULT_SENDER')
MAIL_PORT = env.int('MAIL_PORT')
MAIL_USE_SSL = env.bool('MAIL_USE_SSL')
MAIL_USE_TLS = env.bool('MAIL_USE_TLS')
MAIL_DEBUG = env.int('MAIL_DEBUG')

# Celery
CELERY_BROKER_URL = env('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = env('CELERY_RESULT_BACKEND')
CELERY_SEND_TASK_SENT_EVENT = env('CELERY_SEND_TASK_SENT_EVENT')
SERVER_NAME = env('SERVER_NAME')
