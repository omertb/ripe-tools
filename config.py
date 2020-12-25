# default config
import os


class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = os.environ['FLASKSECRETKEY']


class DevelopmentConfig(BaseConfig):
    SESSION_COOKIE_SECURE = False
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
    # session headers
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    SESSION_COOKIE_SECURE = True
