# Third Party Libraries
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Local Libraries
from .config import Config

# Create database instance
db = SQLAlchemy()


def create_app():
    """
    Application constructor.

    Creates and configures the Flask app instance and
    initializes extensions (database, migrations, etc.)

    Args:
        None

    Returns:
        Flask: the configured Flask app instance.
    """
    # Create the flask app instance
    app = Flask(__name__)

    # Import config
    app.config.from_object(Config)

    # Initalize database with the app
    db.init_app(app)
    migrate = Migrate(app, db)  # noqa: F841

    from . import models  # noqa: F401

    return app
