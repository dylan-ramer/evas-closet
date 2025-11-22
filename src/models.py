from src import db
from sqlalchemy import Enum
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timezone

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(32), nullable=False)
    last_name = db.Column(db.String(32))
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(10), index=True, default='basic')

    closet = db.relationship('Catalog', backref='owner', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f"<User {self.username}>"
    
class Catalog(db.Model):
    __tablename__ = 'catalog'

    #Clothing Data
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, nullable=False)
    img_name = db.Column(db.String(128), index=True, default='def.png')
    category = db.Column(Enum("Bra", "Hat", "Outerwear", "Pants", "Shirt", "Shoes", "Shorts", "Socks", "Underwear", name="category_enum"), nullable=False)
    color = db.Column(Enum("Black", "White", "Gray", "Brown", "Tan", "Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink", name="color_enum"), nullable=False)
    size = db.Column(db.String(4), index=True, nullable=False)
    times_worn = db.Column(db.Integer, index=True, default=0)
    last_worn = db.Column(db.DateTime, index=True)
    priority = db.Column(db.Integer, index=True, default=3)
    
    #Owner Data
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f"<Item {self.name}>"
    
class Action(db.Model):
    #Action Type Constants
    LOGIN = "User Login"
    ADD_ITEM = "Add Item"
    EDIT_ITEM = "Edit Item"
    DELETE_ITEM = "Delete Item"
    ADMIN_EDIT_ITEM = "Admin Edit Item"
    ADMIN_DELETE_ITEM = "Admin Delete Item"
    ADMIN_EDIT_USER = "Admin Edit User"
    ADMIN_PRUNE_LOG = "Admin Pruned Log History"
    EXPORT_LOGS = "Export Logs CSV"

    __tablename__ = 'actions'

    #Action Data
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.now(timezone.utc))
    action_type = db.Column(db.String(50), index=True)

    #Actor Data
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    #Target Data
    target_type = db.Column(db.String(50))
    target_id = db.Column(db.Integer)
    details = db.Column(db.String(256))

    def __repr__(self):
        return f"<Action {self.action_type} by ID: {self.user_id}>"