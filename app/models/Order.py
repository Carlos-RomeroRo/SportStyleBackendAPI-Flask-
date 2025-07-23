from enum import Enum
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class OrderStatus(Enum):
    PENDING = "pending"
    PAID = "paid"
    SHIPPED = "shipped"


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    total_price = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Enum(OrderStatus), default=OrderStatus.PENDING, nullable=False)
    items = db.relationship('OrderItem', backref='order', lazy=True)
    
