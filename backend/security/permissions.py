from functools import wraps
from flask import request, jsonify
from security.auth import verify_token

def role_required(allowed_roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            token = request.headers.het('Authorization')
            if not token:
                return jsonify({'message': 'Token is missing'}), 403
            payload = verify_token(token)
            if not payload or payload['role'] not in allowed_roles:
                return jsonify({'message': 'Access denied'}), 403
            return f(*args, **kwargs)
        return decorated_function
    return decorator