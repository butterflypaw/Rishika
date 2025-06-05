# app.py
from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.errors import InvalidId

app = Flask(__name__)

# MongoDB Configuration
client = MongoClient('mongodb://localhost:27017/')
db = client['library']
books_collection = db['books']

# Utility function to convert MongoDB ObjectId to string
def serialize_book(book):
    return {
        'id': str(book['_id']),
        'title': book['title'],
        'author': book['author'],
        'published_year': book['published_year']
    }

# Create a new book
@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    if not data or not all(k in data for k in ('title', 'author', 'published_year')):
        return jsonify({'error': 'Invalid input'}), 400

    book = {
        'title': data['title'],
        'author': data['author'],
        'published_year': data['published_year']
    }
    result = books_collection.insert_one(book)
    book['_id'] = result.inserted_id
    return jsonify(serialize_book(book)), 201

# Read all books
@app.route('/books', methods=['GET'])
def get_books():
    books = books_collection.find()
    return jsonify([serialize_book(book) for book in books]), 200

# Read a single book by ID
@app.route('/books/<id>', methods=['GET'])
def get_book(id):
    try:
        book = books_collection.find_one({'_id': ObjectId(id)})
        if not book:
            return jsonify({'error': 'Book not found'}), 404
        return jsonify(serialize_book(book)), 200
    except InvalidId:
        return jsonify({'error': 'Invalid book ID'}), 400

# Update a book by ID
@app.route('/books/<id>', methods=['PUT'])
def update_book(id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid input'}), 400

        updated_fields = {k: v for k, v in data.items() if k in ('title', 'author', 'published_year')}
        if not updated_fields:
            return jsonify({'error': 'No valid fields to update'}), 400

        result = books_collection.update_one({'_id': ObjectId(id)}, {'$set': updated_fields})
        if result.matched_count == 0:
            return jsonify({'error': 'Book not found'}), 404

        book = books_collection.find_one({'_id': ObjectId(id)})
        return jsonify(serialize_book(book)), 200
    except InvalidId:
        return jsonify({'error': 'Invalid book ID'}), 400

# Delete a book by ID
@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    try:
        result = books_collection.delete_one({'_id': ObjectId(id)})
        if result.deleted_count == 0:
            return jsonify({'error': 'Book not found'}), 404
        return jsonify({'message': 'Book deleted successfully'}), 200
    except InvalidId:
        return jsonify({'error': 'Invalid book ID'}), 400

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

# Main function to run the app
if __name__ == '__main__':
    app.run(debug=True)
