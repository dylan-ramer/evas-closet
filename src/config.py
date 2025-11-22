import os

rootdir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

class Config:
    """Flask app configuration variables."""
    
    #Database Config Settings
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(rootdir, 'closet.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False