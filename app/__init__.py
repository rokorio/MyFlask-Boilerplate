from flask import Flask
from app.extensions import db,login_manager, migrate,cache
from app.config import Config

def create_app(config_class=Config):
    app=Flask(__name__)
    app.config.from_object(config_class)


    # Init Extensions

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app,db)
    cache.init_app(app)

    # Register Bluprints

    from app.blueprints.auth  import auth_bp
    from app.blueprints.trading import trading_bp
    from app.blueprints.admin import admin_bp
    from app.blueprints.api.v1 import api_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(trading_bp, url_prefix="/trading")
    app.register_blueprint(admin_bp, url_prefix="/admin")
    app.register_blueprint(api_bp, url_prefix="/api/v1")

    #Register error handlers
    from app.utils.errors import register_errors
    register_errors(app)

    return app

