from app.models.OrderItems import OrderItem 
from app.config import ma

class OrderItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = OrderItem
        load_instance = True
        include_fk = True

order_item_schema = OrderItemSchema()
order_items_schema = OrderItemSchema(many=True)