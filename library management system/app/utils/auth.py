from flask import request, jsonify

AUTH_TOKEN = "secure_token"

def token_required(f):
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if token != AUTH_TOKEN:
            return jsonify({'message': 'Unauthorized access'}), 401
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper
