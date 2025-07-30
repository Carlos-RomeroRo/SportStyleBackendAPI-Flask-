from app.config import db
from app.models.Order import Order, OrderStatus
from app.models.User import User
from datetime import datetime, timedelta
import random

def seed_orders():
    if not Order.query.first():

        user_ids = [user.id for user in User.query.all()]
        def random_date_within_last_days(days=30):
            return datetime.utcnow() - timedelta(days=random.randint(0, days))

        orders = [
            Order(user_id=user_ids[0], total_price=59.98, status=OrderStatus.PENDING, date=random_date_within_last_days()),
            Order(user_id=user_ids[1], total_price=39.99, status=OrderStatus.PAID,  date=random_date_within_last_days()),
            Order(user_id=user_ids[2], total_price=89.99, status=OrderStatus.PENDING,  date=random_date_within_last_days()),
            Order(user_id=user_ids[3], total_price=22.00, status=OrderStatus.SHIPPED,  date=random_date_within_last_days()),
            Order(user_id=user_ids[4], total_price=15.99, status=OrderStatus.PAID,  date=random_date_within_last_days())
        ]
        db.session.add_all(orders)
        db.session.commit()
        print("Se han insertado las órdenes del SEED en la base de datos.")
    else:
        print("La tabla de órdenes ya tiene registros, No se intertaron datos del SEED.")