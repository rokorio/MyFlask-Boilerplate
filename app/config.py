import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY=os.getenv('SECRET_KEY' , 'dev-key-change-me')
    SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URL':'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False

    #for you trading app
    MT5_LOGIN=os.getenv('MT5_LOGIN')
    CACHE_TYPE ='SimpleCache'

class DevelopmentConfig(Config):
    DEBUG=True

class ProductionConfig(Config):
    DEBUG=False
    SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URL') #Postgres

class TestingConfig(Config):
    TESTING=True
    SQLALCHEMY_DATABASE_URI='sqlite:///:memory'