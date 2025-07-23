from flask_marshmallow import Marshmallow
from models.Order import Order  

ma = Marshmallow()

class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order
        load_instance = True
        include_fk = True
    
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)