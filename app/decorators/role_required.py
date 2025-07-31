from flask_jwt_extended import get_jwt, verify_jwt_in_request
from functools import wraps
from flask import jsonify

def role_required(*allowed_roles):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            jwt_data = get_jwt()
            user_role = jwt_data.get('role')

            if user_role not in allowed_roles:
                return jsonify({"msg": "Acceso denegado"}), 403
            
            return fn(*args, **kwargs)
        return decorator
    return wrapper
