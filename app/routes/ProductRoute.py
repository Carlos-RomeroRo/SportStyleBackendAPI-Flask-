from flask import Blueprint, jsonify, request
from app.services.ProductService import (
    create_product,
    get_product_by_id,
    get_all_products,
    update_product,
    delete_product
)

product_bp = Blueprint('product_bp', __name__)
@product_bp.route('/create', methods=['POST'])
def create_product_route():
    product_data = request.get_json()
    product = create_product(product_data)
    return jsonify(product), 201

@product_bp.route('/getById/<int:product_id>', methods=['GET'])
def get_product_by_id_route(product_id):
    product = get_product_by_id(product_id)
    if product:
        return jsonify(product),200
    return jsonify({"message": "Product not found"}), 404

@product_bp.route('/updateById/<int:product_id>', methods=['PUT'])
def update_product_route(product_id):
    product_data = request.get_json()
    product = update_product(product_id, product_data)
    if product:
        return jsonify(product), 200
    return jsonify({"message": "Product not found"}), 404

@product_bp.route('/delete_product/<int:product_id>', methods=['DELETE'])
def delete_product_route(product_id):
    success = delete_product(product_id)
    if success:
        return jsonify({"message": "Product deleted successfully"}), 204
    return jsonify({"message": "Product not found"}), 404

@product_bp.route('/getAll', methods=['GET'])
def get_all_products_route():
    products = get_all_products()
    return jsonify(products), 200