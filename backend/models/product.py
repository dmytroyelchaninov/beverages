from backend import db
from backend.models.tag import Tag, product_tags
from backend.models.category import Subcategory

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    
    subcategory_id = db.Column(db.Integer, db.ForeignKey('subcategories.id'), nullable=False)
    subcategory = db.relationship('Subcategory', backref='products')

    tags = db.relationship('Tag', secondary=product_tags, lazy='subquery',
                           backref=db.backref('products', lazy=True))

    def __repr__(self):
        return f'<Product {self.name}>'