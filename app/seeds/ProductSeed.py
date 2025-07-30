from app.config import db
from app.models.Product import Product
from app.models.Category import Category

def seed_products():
    if not Product.query.first():
        category_ids = [cat.id for cat in Category.query.all()]
        products = [
                 Product(
                    name="Camiseta Dry-Fit Hombre",
                    description="Camiseta deportiva de secado rápido para hombres",
                    price=29.99,
                    stock=50,
                    size="M",
                    color="Azul",
                    category_id=category_ids[0]
                ),
                Product(
                    name="Leggings Compresivos Mujer",
                    description="Leggings deportivos elásticos y cómodos",
                    price=39.99,
                    stock=40,
                    size="S",
                    color="Negro",
                    category_id=category_ids[1]
                ),
                Product(
                    name="Zapatillas Running Pro",
                    description="Zapatillas ligeras para correr largas distancias",
                    price=89.99,
                    stock=30,
                    size="42",
                    color="Blanco",
                    category_id=category_ids[2]
                ),
                Product(
                    name="Gorra Ajustable Nike",
                    description="Gorra deportiva negra con visera curva",
                    price=22.00,
                    stock=25,
                    size="Única",
                    color="Negra",
                    category_id=category_ids[3]
                ),
                Product(
                    name="Guantes de Gimnasio Antideslizantes",
                    description="Guantes acolchados para levantamiento de pesas",
                    price=15.99,
                    stock=35,
                    size="L",
                    color="Gris",
                    category_id=category_ids[4]
                )
        ]
        db.session.add_all(products)
        db.session.commit()
        print("Se han insertado los productos del SEED en la base de datos.")
    else:
        print("La tabla de productos ya tiene registros, No se intertaron datos del SEED.")