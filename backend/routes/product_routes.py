from flask import Blueprint, jsonify, request
from backend.services.product_service import add_product, get_all_products, get_product_by_id, update_product, delete_product

products_bp = Blueprint('products', __name__, url_prefix='/api/products')

@products_bp.route('/add_product', methods=['POST'])
def add_product_route():
    data = request.json
    new_product = add_product(data)
    return jsonify({'message': 'Product added successfully!', 'product_id': new_product.id}), 201

@products_bp.route('/get_products', methods=['GET'])
def get_products_all():
    products = get_all_products()
    products_list = []
    for product in products:
        product_data = {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'stock': product.stock,
            'description': product.description,
            'tags': [tag.name for tag in product.tags]  # Include product-specific tags
        }
        products_list.append(product_data)
    
    return jsonify({'products': products_list}), 200

@products_bp.route('/update_product/<int:product_id>', methods=['PUT'])
def update_product_route(product_id):
    product = get_product_by_id(product_id)
    data = request.json
    updated_product = update_product(product, data)
    
    return jsonify({'message': 'Product updated successfully!', 'product_id': updated_product.id}), 200

@products_bp.route('/delete_product/<int:product_id>', methods=['DELETE'])
def delete_product_route(product_id):
    product = get_product_by_id(product_id)
    delete_product(product)
    
    return jsonify({'message': 'Product deleted successfully!'}), 204