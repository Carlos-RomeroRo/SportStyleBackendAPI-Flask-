from flask_marshmallow import Marshmallow
from models.Category import  Category 

ma = Marshmallow()

class CategorySchema(ma.Schema):
    class Meta:
        model = Category
        load_instance = True
        include_fk = True
    

