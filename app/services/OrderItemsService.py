from flask import abort
from models.OrderItems import db, OrderItems
from schemas.OrderItemSchema import order_item_schema, order_items_schema


def create_order_items(order_items):
    try:
        orderItems = order_item_schema.load(order_items)
        db.session.add(orderItems)
        db.session.commit()
        return order_item_schema.dump(orderItems)
    except Exception as e:
        print(e)
        abort(400, description="Error creating order items")

def get_order_items_by_id(order_items_id):
    orderItems = OrderItems.query.get(order_items_id)
    if not orderItems:
        abort(404, description="Order items not found")
    return order_item_schema.dump(orderItems)

def get_all_order_items():
    orderItems = OrderItems.query.all()
    return order_items_schema.dump(orderItems)

def update_order_items(order_items_id, order_items):
    orderItems = OrderItems.query.get(order_items_id)
    if not orderItems:
        abort(404, description="Order items not found")
    try:
        update_data = order_item_schema.load(order_items, session=db.session, partial=True)
        for attr in order_items:
            setattr(orderItems, attr, getattr(update_data, attr))
        db.session.commit()
        return order_item_schema.dump(orderItems)
    except Exception as e:
        print(e)
        abort(400, description="Error updating order items")

def delete_order_items(order_items_id):
    orderItems = OrderItems.query.get(order_items_id)
    if not orderItems:
        abort(404, description="Order items not found")
    db.session.delete(orderItems)
    db.session.commit()
    return {"message": "Order items deleted successfully"}