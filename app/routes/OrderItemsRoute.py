from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.decorators.role_required import role_required
from app.services.OrderItemsService import(
    create_order_items,
    get_order_items_by_id,
    get_all_order_items,
    update_order_items,
    delete_order_items
)

order_items_bp = Blueprint('order_items_bp', __name__)

@order_items_bp.route('/create', methods=['POST'])
@jwt_required()
def create_order_item_route():
    order_item_data = request.get_json()
    order_item = create_order_items(order_item_data)
    return jsonify(order_item), 201

@order_items_bp.route('/getById/<int:order_item_id>', methods=['GET'])
@jwt_required()
@role_required("admin", "superadmin")
def get_order_item_by_id_route(order_item_id):
    order_item = get_order_items_by_id(order_item_id)
    return jsonify(order_item), 200

@order_items_bp.route('/getAll', methods=['GET'])
@jwt_required()
@role_required("admin", "superadmin")
def get_all_order_items_route():
    order_items = get_all_order_items()
    return jsonify(order_items), 200


@order_items_bp.route('/updateById/<int:order_item_id>', methods=['PUT'])
@jwt_required()
@role_required("admin", "superadmin")
def update_order_items_route(order_item_id):
    order_item_data = request.get_json()
    order_item = update_order_items(order_item_id, order_item_data)
    if order_item:
        return jsonify(order_item), 200
    return jsonify({"message": "Order item not found"}), 404

@order_items_bp.route('/deleteById/<int:order_item_id>', methods=['DELETE'])
@jwt_required()
@role_required("admin", "superadmin")
def delete_order_items_route(order_item_id):
    sucess = delete_order_items(order_item_id)
    if sucess:
        return jsonify({"message": "Order item deleted successfully"}), 200
    return jsonify({"message": "Order item not found"}), 404