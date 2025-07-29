
from marshmallow_enum import EnumField
from app.models.Order import Order, OrderStatus  
from app.config import ma

class OrderSchema(ma.SQLAlchemyAutoSchema):

    status = EnumField(OrderStatus, by_value=True)  # Agrega esta línea
    class Meta:
        model = Order
        load_instance = True
        include_fk = True
    
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)
