"""Main configuration file"""
# Define the application directory
import os


class LocalConfig(object):
    """
    This is a class for base configuration for the project
    """

    # Statement for enabling the development environment
    DEBUG = True

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Define the database - we are working with
    # SQLite for this example
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "app.db")
    # To disable tracking modifications on Objects by Flask-SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATABASE_CONNECT_OPTIONS = {}
    JSON_SORT_KEYS = False
    # Application threads. A common general assumption is
    # using 2 per available processor cores - to handle
    # incoming requests using one and performing background
    # operations using the other.
    THREADS_PER_PAGE = 2

    # Enable protection again *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED = True

    # Use a secure, unique and absolutely secret key for
    # signing the data.
    CSRF_SESSION_KEY = "secret"

    # Secret key for signing cookies
    SECRET_KEY = "secret"

    AUTH_TOKEN_TTL_MINUTES = 60
    JWT_SECRET_KEY = "M0n3Y_H3!5T"

    HOOKS_REQUIRED = True

    # Logs
    LOG_LEVEL = 'DEBUG'
    LOG_FILE_PATH = "app/logger/logs"


class StagingConfig(LocalConfig):
    """
    Class containing configuration for staging environment
    """
    SECRET_KEY = "staging-secret"
    CSRF_SESSION_KEY = "staging-csrf-secret"
    DEBUG = False

    # Logs
    LOG_LEVEL = 'DEBUG'
    LOG_FILE_PATH = "app/logger/logs"


class ProductionConfig(LocalConfig):
    """
    Class containing configuration for production environment
    """
    SECRET_KEY = "prod-secret"
    CSRF_SESSION_KEY = "production-csrf-secret"
    DEBUG = False

    # Logs
    LOG_LEVEL = 'INFO'
    LOG_FILE_PATH = "app/logger/logs"


APP_ENV_CONFIGS = {
    "local": "config.LocalConfig",
    "production": "config.ProductionConfig",
    "staging": "config.StagingConfig"
}
