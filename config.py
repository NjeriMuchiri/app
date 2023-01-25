class Config(object):
    DEBUG = False
    TESTING = False
    
    SECRET_KEY = '\xba\xc6H\x9a\x96d\xfe\x1c\xb2\xe4\xfb\xb9\xac\xa0\xaf'
    DB_NAME = "production-db"
    BD_USERNAME = "root"
    DB_PASSWORD = "example"
    
    UPLOADS = "/home/muchirinjeri/app/app/static/images/uploads"
    
    SESSION_COOKIE_SECURE = True
    
    
class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    
    DB_NAME = "development-db"
    BD_USERNAME = "root"
    DB_PASSWORD = "example"
    
    UPLOADS = "/home/muchirinjeri/app/app/static/img/uploads"
    
    SESSION_COOKIE_SECURE = False
    
class TestingConfig(Config):
    TESTING = True
    
    DB_NAME = "development-db"
    BD_USERNAME = "root"
    DB_PASSWORD = "example"
    
    UPLOADS = "/home/muchirinjeri/app/app/static/img/uploads"
    
    SESSION_COOKIE_SECURE = False
    
    