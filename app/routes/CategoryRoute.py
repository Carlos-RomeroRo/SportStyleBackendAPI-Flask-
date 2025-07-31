from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.decorators.role_required import role_required
from app.services.CategoryService import (
    create_category,
    get_category_by_id,
    get_all_categories,
    update_category,
    delete_category
)

category_bp = Blueprint('category_bp', __name__)

@category_bp.route('/create', methods=['POST'])
@jwt_required()
def create_category_route():
    category_data = request.get_json()
    category = create_category(category_data)
    return jsonify(category), 201

@category_bp.route('/getById/<int:category_id>', methods=['GET'])
@jwt_required()
@role_required("admin", "superadmin")
def get_category_by_id_route(category_id):
    category = get_category_by_id(category_id)
    if category:
        return jsonify(category), 200
    return jsonify({"message": "Category not found"}), 404

@category_bp.route('/updateById/<int:category_id>', methods=['PUT'])
@jwt_required()
@role_required("admin", "superadmin")
def update_category_route(category_id):
    category_data = request.get_json()
    category = update_category(category_id, category_data)
    if category:
        return jsonify(category), 200
    return jsonify({"message": "Category not found"}), 404

@category_bp.route('/deleteById/<int:category_id>', methods=['DELETE'])
@jwt_required()
@role_required("admin", "superadmin")
def delete_category_route(category_id):
    success = delete_category(category_id)
    if success:
        return jsonify({"message": "Category deleted successfully"}), 204
    return jsonify({"message": "Category not found"}), 404

@category_bp.route('/getAll', methods=['GET'])
@jwt_required()
def get_all_categories_route():
    categories = get_all_categories()
    return jsonify(categories), 200