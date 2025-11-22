from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create database instance
db = SQLAlchemy()

def create_app():
    # Create the flask app instance
    app = Flask(__name__)

    # Import config
    app.config.from_object(Config)

    # Initalize database with the app
    db.init_app(app)
    migrate = Migrate(app, db)

    from . import models

    return app