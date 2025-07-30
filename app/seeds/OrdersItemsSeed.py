from app.config import db
from app.models.OrderItems import OrderItem
from app.models.Order import Order
from app.models.Product import Product


def seed_order_items():
    if not OrderItem.query.first():

        order_ids = [order.id for order in Order.query.all()]
        product_ids = [product.id for product in Product.query.all()]

        order_items = [
                    OrderItem(order_id=order_ids[0], product_id =  product_ids[0], quantity=14),
                    OrderItem(order_id=order_ids[1], product_id =  product_ids[2], quantity=15),
                    OrderItem(order_id=order_ids[2], product_id =  product_ids[1], quantity=10),
                    OrderItem(order_id=order_ids[3], product_id =  product_ids[4], quantity=12),
                    OrderItem(order_id=order_ids[4], product_id =  product_ids[3], quantity=5),
        ]
        db.session.add_all(order_items)
        db.session.commit()
        print("Se han insertado los items de pedidos del SEED en la base de datos.")
    else:
        print("La tabla de items de pedidos ya tiene registros, No se intertaron datos del SEED.")