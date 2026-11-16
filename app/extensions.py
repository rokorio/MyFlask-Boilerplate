from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_caching import Cache

db=SQLAlchemy()
login_manager=LoginManager()
login_manager.login_view='auth.login'
migrate=Migrate()
cache=Cache()