from flask import abort
from app.models.OrderItems import db, OrderItem
from app.schemas.OrderItemSchema import order_item_schema, order_items_schema


def create_order_items(order_items):
    
    try:
        orderItems = order_item_schema.load(order_items)
        db.session.add(orderItems)
        db.session.commit()
        return order_item_schema.dump(orderItems)
    except Exception as e:
        import traceback
        traceback.print_exc()  # <--- imprime la traza completa
        print(e)               # <--- imprime el mensaje de error
        abort(400, description=str(e))  # <--- muestra el error real al cliente

def get_order_items_by_id(order_items_id):
    orderItems = OrderItem.query.get(order_items_id)
    if not orderItems:
        abort(404, description="Order items not found")
    return order_item_schema.dump(orderItems)

def get_all_order_items():
    orderItems = OrderItem.query.all()
    return order_items_schema.dump(orderItems)

def update_order_items(order_items_id, order_items):
    orderItems = OrderItem.query.get(order_items_id)
    if not orderItems:
        abort(404, description="Order items not found")
    try:
        update_data = order_item_schema.load(order_items, session=db.session, partial=True)
        for attr, value in update_data.__dict__.items():
            if attr != '_sa_instance_state':
                setattr(orderItems, attr, value)
        db.session.commit()
        return order_item_schema.dump(orderItems)
    except Exception as e:
        print(e)
        abort(400, description="Error updating order items")

def delete_order_items(order_items_id):
    orderItems = OrderItem.query.get(order_items_id)
    if not orderItems:
        abort(404, description="Order items not found")
    db.session.delete(orderItems)
    db.session.commit()
    return {"message": "Order items deleted successfully"}