from app.models.Order import db, Order
from app.schemas.OrderSchema import order_schema, orders_schema 
from flask import abort

def create_order(order):
    try:
        order = order_schema.load(order)
        db.session.add(order)
        db.session.commit()
        return order_schema.dump(order)
    except Exception as e:
        import traceback
        traceback.print_exc()  # <--- imprime la traza completa
        print(e)               # <--- imprime el mensaje de error
        abort(400, description=str(e))  # <--- muestra el error real al cliente
        
def get_order_by_id(order_id):
    order = Order.query.get(order_id)
    if not order:
        abort(404, description="Order not found")
    return order_schema.dump(order)

def get_all_orders():
    orders = Order.query.all()
    return orders_schema.dump(orders)

def update_order(order_id, order_data):
    order = Order.query.get(order_id)
    if not order:
        abort(404, description="Order not found")
    try:
        update_data = order_schema.load(order_data, session=db.session, partial=True)
        for attr, value in update_data.__dict__.items():
            setattr(order, attr, value)
        db.session.commit()
        return order_schema.dump(order)
    except Exception as e:
        print(e)
        abort(400, description="Error updating order")

def delete_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        abort(404, description="Order not found")
    db.session.delete(order)
    db.session.commit()
    return {"message": "Order deleted successfully"}