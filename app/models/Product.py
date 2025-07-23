from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    size = db.Column(db.String(20), nullable=False)
    color = db.Column(db.String(30), nullable=False)
    
    #Foreing Key (Realtionship with category table)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('products', lazy=True))
    
    def __repr__(self):
        return f"Product('{self.name}', '{self.description}', '{self.price}', '{self.stock}', '{self.size}', '{self.color}')"