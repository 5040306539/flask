import os


class Config:
    SQLALCHEMY_DATABASE_URI =os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS =os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS',False)


class Development(Config):
    print("loading Development config")
    DEBUG = True


class Pordution(Config):
    print("loading pordiction config")
    DEBUG = False
