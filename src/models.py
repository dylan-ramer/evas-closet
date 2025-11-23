from datetime import datetime, timezone

from sqlalchemy import Enum
from werkzeug.security import check_password_hash, generate_password_hash

from src import db


class User(db.Model):
    """
    Represents a single user account,
    storing authentication details and user information

    Attributes:
        id (int): Primary key.
        first_name (str): User's first name.
        last_name (str): (OPTIONAL) User's last name.
        username (str): User's unique username.
        email (str): User's email address.
        password_hash (str): User's hashed and salted password.
        role (str): User's role. Must be defined in ``role_enum``.
        closet (Query): Relationship to user's catalog items.
    """

    __tablename__ = "users"

    # User Data
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(32), nullable=False)
    last_name = db.Column(db.String(32))
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(
        Enum("basic", "admin", name="role_enum"), index=True, default="basic"
    )

    # Catalog relationship
    closet = db.relationship("Catalog", backref="owner", lazy="dynamic")

    # Updates database with new hashed and salted password
    def set_password(self, password):
        """
        Salt, hash, and store the user's password.

        Args:
            password (str): The user's raw password to hash.

        Returns:
            None
        """
        self.password_hash = generate_password_hash(password)

    # Verify given password matches stored password
    def check_password(self, password):
        """
        Verify the given raw password against the stored password hash.

        Args:
            password (str): The user's raw password to verify.

        Returns:
            bool: ``True`` if the password matches, ``False`` otherwise.
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.username}>"


class Catalog(db.Model):
    """
    Represents a single item in the catalog, including metadata and item attributes

    Attributes:
        id (int): Primary key.
        name (str): Name of clothing item.
        img_name (str): (OPTIONAL) Name of saved image file.
        category (str): The category of the item. Must be defined in ``category_enum``.
        color (str): The color of the item. Must be defined in ``color_enum``.
        size (str): The size of the item. Supports alphabetic and numeric input.
        times_worn (int): The number of times the item has been worn. Default is 0.
        last_worn (datetime): (OPTIONAL) Date/time item was worn last.
        priority (int): The priority value of the item. 1 (highest) - 5 (lowest).
        user_id (int): ID of item owner. Foreign key related to users.id.
    """

    __tablename__ = "catalog"

    # Clothing Data
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, nullable=False)
    img_name = db.Column(db.String(128), index=True, default="def.png")
    category = db.Column(
        Enum(
            "Bra",
            "Hat",
            "Outerwear",
            "Pants",
            "Shirt",
            "Shoes",
            "Shorts",
            "Socks",
            "Underwear",
            name="category_enum",
        ),
        nullable=False,
    )
    color = db.Column(
        Enum(
            "Black",
            "White",
            "Gray",
            "Brown",
            "Tan",
            "Red",
            "Orange",
            "Yellow",
            "Green",
            "Blue",
            "Purple",
            "Pink",
            name="color_enum",
        ),
        nullable=False,
    )
    size = db.Column(db.String(4), index=True, nullable=False)
    times_worn = db.Column(db.Integer, index=True, default=0)
    last_worn = db.Column(db.DateTime, index=True)
    priority = db.Column(db.Integer, index=True, default=3)

    # Owner Data
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __repr__(self):
        return f"<Item {self.name}>"


class Action(db.Model):
    """
    Tracks user interaction with catalog items,
    and admin interaction with catalog items and users

    Attributes:
        id (int): Primary key.
        action_type (ActionType): Type of interaction performed.
        user_id (int): ID of acting user. Foreign key related to users.id.
        target_type (TargetType): Type of target interacted with.
        target_id (int): ID of target interacted with.
        details (string): (OPTIONAL) Interaction justification.
        timestamp (datetime): Date/time when interaction occured.
    """

    __tablename__ = "actions"

    # Action Type Constants
    LOGIN = "User Login"
    ADD_ITEM = "Add Item"
    EDIT_ITEM = "Edit Item"
    DELETE_ITEM = "Delete Item"
    ADMIN_EDIT_ITEM = "Admin Edit Item"
    ADMIN_DELETE_ITEM = "Admin Delete Item"
    ADMIN_EDIT_USER = "Admin Edit User"
    ADMIN_PRUNE_LOG = "Admin Pruned Log History"
    EXPORT_LOGS = "Export Logs CSV"

    # Action Data
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.now(timezone.utc))
    action_type = db.Column(db.String(50), index=True)

    # Actor Data
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    # Target Data
    target_type = db.Column(db.String(50))
    target_id = db.Column(db.Integer)
    details = db.Column(db.String(256))

    def __repr__(self):
        return f"<Action {self.action_type} by ID: {self.user_id}>"
