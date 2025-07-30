from app.config import db
from app.models.Category import Category


def seed_categories():
    if not Category.query.first():
        categories = [
            Category(name="Camisetas Deportivas", description="Camisetas transpirables para entrenamiento y competencia"),
            Category(name="Pantalones Deportivos", description="Pantalones, leggings y shorts para actividades físicas"),
            Category(name="Calzado Deportivo", description="Zapatillas para running, fútbol, baloncesto y más"),
            Category(name="Accesorios Deportivos", description="Gorras, muñequeras, bandas para la cabeza y mochilas"),
            Category(name="Equipamiento Fitness", description="Guantes de gimnasio, cinturones, botellas deportivas"),
        ]
        db.session.add_all(categories)
        db.session.commit()
        print("Se han insertado las categorías del SEED en la base de datos.")
    else:
        print("La tabla de categorías ya tiene registros, No se intertaron datos del SEED.")