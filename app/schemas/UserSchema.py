from app.models.User import User 
from app.config import ma
from app.models.User import UserRole
from marshmallow_enum import EnumField

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        include_fk = True
    role = EnumField(UserRole, by_value=True) 

user_schema = UserSchema()
users_schema = UserSchema(many=True)