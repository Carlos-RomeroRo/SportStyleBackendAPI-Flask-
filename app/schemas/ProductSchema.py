from flask_marshmallow import Marshmallow
from models.Product import Product  

ma = Marshmallow()

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True
        include_fk = True