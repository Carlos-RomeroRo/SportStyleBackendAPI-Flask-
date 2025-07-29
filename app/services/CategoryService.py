from app.models.Category import db, Category
from app.schemas.CategorySchema import category_schema, categories_schema
from flask import abort

def create_category(category_data):
    try:
        category = category_schema.load(category_data)
        db.session.add(category)
        db.session.commit()
        return category_schema.dump(category)
    except Exception as e:
        import traceback
        traceback.print_exc()  # <--- imprime la traza completa
        print(e)               # <--- imprime el mensaje de error
        abort(400, description=str(e))  # <--- muestra el error real al cliente


def get_category_by_id(category_id):
    category = Category.query.get(category_id)
    if not category:
        abort(404, description="Category not found")
    return category_schema.dump(category)

def get_all_categories():
    categories = Category.query.all()
    return categories_schema.dump(categories)

def update_category(category_id, category_data):
    category = Category.query.get(category_id)
    if not category:
        abort(404, description="Category not found")
    try:
        update_data = category_schema.load(category_data, session=db.session, partial=True)
        for attr, value in update_data.__dict__.items():
            if attr != '_sa_instance_state':
                setattr(category, attr, value)
        db.session.commit()
        return category_schema.dump(category)
    except Exception as e:
        print(e)
        abort(400, description="Error updating category")

def delete_category(category_id):
    category = Category.query.get(category_id)
    if not category:
        abort(404, description="Category not found")
    db.session.delete(category)
    db.session.commit()
    return {"message": "Category deleted successfully"}