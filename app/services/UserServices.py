from app.models.User import db, User
from app.schemas.UserSchema import user_schema, users_schema
from flask import abort

def create_user(user_data):
    try:
        user = user_schema.load(user_data)
        db.session.add(user)
        db.session.commit()
        return user_schema.dump(user)
    except Exception as e:
        import traceback
        traceback.print_exc()  # <--- imprime la traza completa
        print(e)               # <--- imprime el mensaje de error
        abort(400, description=str(e))  # <--- muestra el error real al cliente

def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if not user:
        abort(404, description="User not found")
    return user_schema.dump(user)

def get_all_users():
    users = User.query.all()
    return users_schema.dump(users)

def update_user(user_id, user_data):
    user = User.query.get(user_id)
    if not user:
        abort(404, description="User not found")
    try:
        update_data = user_schema.load(user_data, session=db.session, partial=True)
        for attr, value in update_data.__dict__.items():
            if attr != '_sa_instance_state':
                setattr(user, attr, value)
        db.session.commit()
        return user_schema.dump(user)
    except Exception as e:
        print(e)
        abort(400, description="Error updating user")

def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        abort(404, description="User not found")
    db.session.delete(user)
    db.session.commit()
    return {"message": "User deleted successfully"}