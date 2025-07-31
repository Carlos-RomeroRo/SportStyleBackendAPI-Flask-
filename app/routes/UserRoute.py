from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.decorators.role_required import role_required
from app.services.UserServices import(
    create_user,
    get_user_by_id,
    update_user,
    delete_user,
    get_all_users
)

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/create',methods=['POST'])
def create_user_route():
    user_data = request.get_json()
    user = create_user(user_data)
    return jsonify(user), 201


@user_bp.route('/getById/<int:user_id>', methods=['GET'])
@jwt_required()
@role_required('admin','superadmin')
def get_user_route(user_id):
    user= get_user_by_id(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"message": "User not found"}), 404


@user_bp.route('/updateById/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user_route(user_id):
    user_data = request.get_json()
    user = update_user(user_id, user_data)
    if user:
        return jsonify(user), 200
    return jsonify({"message": "User not found"}), 404


@user_bp.route('/deleteById/<int:user_id>', methods=['DELETE'])
@jwt_required()
@role_required('admin','superadmin')
def delete_user_route(user_id):
    success = delete_user(user_id)
    if success:
        return jsonify({"message": "User deleted successfully"}), 204
    return jsonify({"message": "User not found"}), 404


@user_bp.route('/getAll',methods=['GET'])
def get_all_users_route():
    users = get_all_users()
    return jsonify(users), 200
