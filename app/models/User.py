import enum
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserRole(enum.Enum):
    ADMIN = "admin"
    USER = "user"
    SUPERADMIN = "superadmin"


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.Enum(UserRole), default=UserRole.USER, nullable=False)

    def __repr__(self):
        return f'<User {self.email}> role: {self.role.name} email: {self.email}>'