from flask_marshmallow import Marshmallow
from models.OrderItems import OrderItems  

ma = Marshmallow()

class OrderItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = OrderItems
        load_instance = True
        include_fk = True

order_item_schema = OrderItemSchema()
order_items_schema = OrderItemSchema(many=True)