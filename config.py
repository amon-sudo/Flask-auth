from decouple import config

DATABASE_URI = config("DATABASE_URL")
if DATABASE_URI.startswith("postgress://"):
    DATABASE_URI= DATABASE_URI.replace("postgres://", "postgresql://", 1)


class Config:
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = config("SECRET_KEY", default= "guess-me")
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATION = False
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    
    
class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    WTF_CSRF_ENABLED = False
    DEBUG_TB_ENABLED= True
    
class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite://tetsdb.sqlite"
    BCRYPT_LOG_ROUNDS = 1
    WTF_CSRF_ENABLED = False
    
class ProdectionConfig(config):
    DEBUG = False
    DEBUG_TB_ENABLED = False