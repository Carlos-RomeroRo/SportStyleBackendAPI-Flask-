# seeds/seed_all.py
from app.seeds.UserSeed import seed_users
from app.seeds.CategoriesSeed import seed_categories
from app.seeds.ProductSeed import seed_products
from app.seeds.OrderSeed import seed_orders
from app.seeds.OrdersItemsSeed import seed_order_items

def run_seed_all():
    print("Iniciando el proceso de SEED...")
    seed_categories()
    seed_products()
    seed_users()
    seed_orders()
    seed_order_items()

    

