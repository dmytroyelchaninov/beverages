from flask import jsonify, request
from backend.models import Product
from backend import db

def add_product(data):
    name = data['name']
    price = float(data['price'])
    stock = int(data['stock'])
    description = data['description']
    
    new_product = Product(name=name, price=price, stock=stock, description=description)
    db.session.add(new_product)
    db.session.commit()
    
    return new_product

def get_all_products():
    return Product.query.all()

def get_product_by_id(product_id):
    return Product.query.get_or_404(product_id)

def update_product(product, data):
    product.name = data['name']
    product.price = float(data['price'])
    product.stock = int(data['stock'])
    product.description = data['description']
    
    db.session.commit()
    return product

def delete_product(product):
    db.session.delete(product)
    db.session.commit()

def get_paginated_products(page, per_page, filters):
    query = Product.query

    if 'category_id'