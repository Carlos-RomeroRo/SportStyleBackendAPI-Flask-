from app.models.Product import Product  
from app.config import ma


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True
        include_fk = True

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)