import enum
from app.config import db


class OrderStatus(enum.Enum):
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

    items = db.relationship('OrderItem', back_populates='order')

    
    
