import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from app.api import api
from app.config import Config

BASEDIR = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
from app.models import *

def create_app():
    
    app = Flask(__name__)
    # Load flask configuration
    config = Config()
    app.config.from_object(config)
    
    # Initialize database and CSRF protection
    db.init_app(app)
    
    # Initialize the flask-restx api
    #api.init_app(app)
    
    # Register blueprint API
    from .api import api_bp
    app.register_blueprint(api_bp)
    
    # Register blueprint
    from .views import register_bp
    register_bp(app)
    
    
    return app