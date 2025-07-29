from app.models.Product import db, Product
from app.schemas.ProductSchema import product_schema, products_schema
from flask import abort

def create_product(product_data):
    try:
        product = product_schema.load(product_data)
        db.session.add(product)
        db.session.commit()
        return product_schema.dump(product)
    except Exception as e:
        import traceback
        traceback.print_exc()  # <--- imprime la traza completa
        print(e)               # <--- imprime el mensaje de error
        abort(400, description=str(e))  # <--- muestra el error real al cliente

def get_product_by_id(product_id):
    product = Product.query.get(product_id)
    if not product:
        abort(404, description="Product not found")
    return product_schema.dump(product)

def get_all_products():
    products = Product.query.all()
    return products_schema.dump(products)

def update_product(product_id, product_data):
    product = Product.query.get(product_id)
    if not product:
        abort(404, description="Product not found")
    try:
        update_data = product_schema.load(product_data, session=db.session, partial=True)
        for attr, value in update_data.__dict__.items():
            if attr != '_sa_instance_state':
                setattr(product, attr, value)
        db.session.commit()
        return product_schema.dump(product)
    except Exception as e:
        print(e)
        abort(400, description="Error updating product")

def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        abort(404, description="Product not found")
    db.session.delete(product)
    db.session.commit()
    return {"message": "Product deleted successfully"}
