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

    if 'category_id' in filters:
        query = query.filter_by(category_id=filters['category_id'])

    if 'subcategory_id' in filters:
        query = query.filter_by(subcategory_id=filters['subcategory_id'])

    if 'min_price' in filters:
        query = query.filter(Product.price.between(filters['min_price'], filters['max_price']))
    
    paginated_products = query.paginate(page=page, per_page=per_page, error_out=False)
    products_list = []
    for product in paginated_products.items:
        product_data = {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'stock': product.stock,
            'description': product.description,
            'tags': [tag.name for tag in product.tags]
        }
        products_list.append(product_data)
    
    return {
        'products': products_list,
        'total_items': paginated_products.total,
        'total_pages': paginated_products.pages,
        'current_page': paginated_products.page
    }