import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from app.config import Config

BASEDIR = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    
    # Load flask configuration
    config = Config()
    app.config.from_object(config)
    
    # Initialize database and CSRF protection
    db.init_app(app)
    
    # Import Models
    from app.models.student import Student
    # Register blueprint
    from .views import register_blueprint
    register_blueprint(app)
    
    return app