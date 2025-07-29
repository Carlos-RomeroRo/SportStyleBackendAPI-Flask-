from flask import Blueprint, request, jsonify
from app.services.OrderService import(
    create_order,
    get_order_by_id,
    get_all_orders,
    update_order,
    delete_order
)

order_bp = Blueprint('order_bp', __name__)

@order_bp.route('/create', methods=['POST'])
def create_order_route():
    order_data = request.get_json()
    order = create_order(order_data)
    return jsonify(order), 201

@order_bp.route('/getById/<int:order_id>', methods=['GET'])
def get_order_by_id_route(order_id):
    order = get_order_by_id(order_id)
    if order:
        return jsonify(order), 200
    return jsonify({"message": "Order not found"}), 404

@order_bp.route('/updateById/<int:order_id>', methods=['PUT'])
def update_order_route(order_id):
    order_data = request.get_json()
    order = update_order(order_id, order_data)
    if order:
        return jsonify(order), 200
    return jsonify({"message": "Order not found"}), 404

@order_bp.route('/deleteById/<int:order_id>', methods=['DELETE'])
def delete_order_route(order_id):
    success = delete_order(order_id)
    if success:
        return jsonify({"message": "Order deleted successfully"}), 204
    return jsonify({"message": "Order not found"}), 404

@order_bp.route('/getAll', methods=['GET'])
def get_all_orders_route():
    orders = get_all_orders()
    return jsonify(orders), 200
