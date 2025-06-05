
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from functools import wraps
from datetime import datetime, timedelta
import jwt

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/altiusinter'
app.config['SECRET_KEY'] = 'your_jwt_secret_key'

mongo = PyMongo(app)
users = mongo.db.users
posts = mongo.db.posts

def token_required(role=None):
    def wrapper(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = None
            if 'Authorization' in request.headers:
                auth = request.headers['Authorization']
                if auth.startswith('Bearer '):
                    token = auth.split(" ")[1]
            if not token:
                return jsonify({'message': 'Token missing'}), 401
            try:
                data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
                current_user = users.find_one({'username': data['username']})
                if not current_user:
                    raise Exception()
                if role and current_user.get('role') != role:
                    return jsonify({'message': 'Forbidden'}), 403
            except:
                return jsonify({'message': 'Invalid token'}), 401
            return f(current_user, *args, **kwargs)
        return decorated
    return wrapper

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    if not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Missing fields'}), 400
    if users.find_one({'username': data['username']}):
        return jsonify({'message': 'User already exists'}), 400
    hashed = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    role = data.get('role', 'user')
    users.insert_one({'username': data['username'], 'password': hashed, 'role': role})
    return jsonify({'message': 'User created'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = users.find_one({'username': data.get('username')})
    if not user or not bcrypt.check_password_hash(user['password'], data['password']):
        return jsonify({'message': 'Invalid credentials'}), 401
    token = jwt.encode({
        'username': user['username'],
        'exp': datetime.utcnow() + timedelta(hours=1)
    }, app.config['SECRET_KEY'], algorithm='HS256')
    return jsonify({'token': token})

@app.route('/posts', methods=['POST'])
@token_required()
def create_post(current_user):
    data = request.get_json()
    if not data.get('title') or not data.get('description'):
        return jsonify({'message': 'Title and description required'}), 400
    post_id = posts.insert_one({
        'title': data['title'],
        'description': data['description'],
        'created_by': current_user['username']
    }).inserted_id
    return jsonify({'message': 'Post created', 'id': str(post_id)}), 201

@app.route('/posts', methods=['GET'])
def get_posts():
    result = []
    for post in posts.find():
        result.append({
            'id': str(post['_id']),
            'title': post['title'],
            'description': post['description'],
            'created_by': post.get('created_by', 'unknown')
        })
    return jsonify(result), 200

@app.route('/posts/<post_id>', methods=['PUT'])
@token_required()
def update_post(current_user, post_id):
    data = request.get_json()
    result = posts.update_one(
        {'_id': ObjectId(post_id)},
        {'$set': {'title': data['title'], 'description': data['description']}}
    )
    if result.matched_count == 0:
        return jsonify({'message': 'Post not found'}), 404
    return jsonify({'message': 'Post updated'}), 200

@app.route('/posts/<post_id>', methods=['DELETE'])
@token_required('admin')
def delete_post(current_user, post_id):
    result = posts.delete_one({'_id': ObjectId(post_id)})
    if result.deleted_count == 0:
        return jsonify({'message': 'Post not found'}), 404
    return jsonify({'message': 'Post deleted'}), 200

@app.route('/profile', methods=['GET'])
@token_required()
def profile(current_user):
    return jsonify({'username': current_user['username'], 'role': current_user['role']})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
