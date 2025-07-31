import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv
from sqlalchemy.orm import DeclarativeBase
from flask_jwt_extended import JWTManager
from datetime import timedelta


db = SQLAlchemy()
ma = Marshmallow()

class Base(DeclarativeBase):
    pass


def create_app():
    app = Flask(__name__)

    load_dotenv()

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=30)
    jwt = JWTManager(app)

    db.init_app(app)
    ma.init_app(app)

    
    from app.models.Category import Category
    from app.models.Product import Product
    from app.models.User import User
    from app.models.Order import Order
    from app.models.OrderItems import OrderItem



    from app.routes.TestRoute import test_bp
    app.register_blueprint(test_bp)

    from app.routes.UserRoute import user_bp
    app.register_blueprint(user_bp, url_prefix="/api/user")

    from app.routes.CategoryRoute import category_bp
    app.register_blueprint(category_bp, url_prefix="/api/category")

    from app.routes.ProductRoute import product_bp
    app.register_blueprint(product_bp, url_prefix="/api/product")

    from app.routes.OrderRoute import order_bp
    app.register_blueprint(order_bp, url_prefix="/api/order")

    from app.routes.OrderItemsRoute import order_items_bp
    app.register_blueprint(order_items_bp, url_prefix="/api/order-item") 

    from app.routes.Login import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/api/login") 
    

    
    print("Rutas registradas:")
    for rule in app.url_map.iter_rules():
        print(rule)

    return app



