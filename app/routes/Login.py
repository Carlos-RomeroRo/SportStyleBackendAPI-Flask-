from flask import request,jsonify, Blueprint
from flask_jwt_extended import create_access_token
from app.models.User import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route('/login', methods=['POST'])
def Login():
    data = request.get_json()
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({"msg": "Missing email or password"}), 400

    email = data['email']
    password = data['password']

    # search user by email || object : class 
    user: User = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"msg": "User not found"}), 404
    
    if user.password != password:  # In a real application, use hashed passwords
        return jsonify({"msg": "Invalid password"}), 401

    access_token = create_access_token(identity=str(user.id), additional_claims={"role": user.role.value})

    return jsonify({
        "token": access_token,
        "user":{
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role.value
        }
    }), 200

    

    