from flask import Blueprint, request, jsonify
from backend.services.user_service import create_user, get_user_by_email, update_user, check_password
from security.permissions import role_required
from security.auth import verify_confirmation_token, generate_token

user_bp = Blueprint('user_bp', __name__, url_prefix='/api/users')

@user_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        user = get_user_by_email(data['email'])
        
        if user:
            if not user.is_confirmed:
                return jsonify({'status': 'error', 'message': 'Please confirm your email'}), 403
            
            if check_password(user, data['password']):
                token = generate_token(user.id, user.user_level.value)
                return jsonify({'status': 'success', 'message': 'Login successful', 'token': token, 'user_id': user.id}), 200
            else:
                return jsonify({'status': 'error', 'message': 'Invalid credentials'}), 401
        else:
            return jsonify({'status': 'error', 'message': 'User not found'}), 404
    except Exception as e:
        return jsonify({'status': 'error', 'message': 'Something went wrong'}), 500

@user_bp.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.get_json()
        
        if get_user_by_email(data['email']):
            return jsonify({'status': 'error', 'message': 'User already exists'}), 400
        
        user = create_user(data)
        return jsonify({'status': 'success', 'message': 'User created successfully', 'user': user.id}), 201
    except Exception as e:
        return jsonify({'status': 'error', 'message': 'Something went wrong'}), 500

@user_bp.route('/confirm/<token>', methods=['GET'])
def confirm_email(token):
    try:
        payload = verify_confirmation_token(token)

        if payload:
            user = get_user_by_email(payload['user_email'])
            if user:
                user.is_confirmed = True
                return jsonify({'status': 'success', 'message': 'Email confirmed'}), 200
            else:
                return jsonify({'status': 'error', 'message': 'User not found'}), 404
        else:
            return jsonify({'status': 'error', 'message': 'Invalid or expired token'}), 400
    except Exception as e:
        return jsonify({'status': 'error', 'message': 'Something went wrong'}), 500

@user_bp.route('/user/<int:user_id>', methods=['PUT'])
@role_required(['admin'])
def update_user_info(user_id):
    try:
        data = request.get_json()
        user = get_user_by_email(data['email'])

        if user:
            updated_user = update_user(user, data)
            return jsonify({'status': 'success', 'message': 'User updated successfully'}), 200
        return jsonify({'status': 'error', 'message': 'User not found'}), 404
    except Exception as e:
        return jsonify({'status': 'error', 'message': 'Something went wrong'}), 500