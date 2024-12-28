from flask import Blueprint, request, jsonify
from app.utils.auth import token_required
from app.utils.helpers import paginate

books_bp = Blueprint('books', __name__)

# In-memory data storage
books = []

@books_bp.route('/', methods=['GET', 'POST'])
@token_required
def manage_books():
    if request.method == 'POST':
        book = request.json
        book['id'] = len(books) + 1
        books.append(book)
        return jsonify({'message': 'Book added successfully', 'book': book}), 201

    elif request.method == 'GET':
        title = request.args.get('title', '').lower()
        author = request.args.get('author', '').lower()
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 5))

        filtered_books = [
            book for book in books
            if (title in book.get('title', '').lower()) or (author in book.get('author', '').lower())
        ]
        paginated_books = paginate(filtered_books, page, per_page)
        return jsonify({
            'books': paginated_books,
            'total_books': len(filtered_books),
            'current_page': page,
            'per_page': per_page
        }), 200

@books_bp.route('/<int:book_id>', methods=['GET', 'PUT', 'DELETE'])
@token_required
def manage_book(book_id):
    for book in books:
        if book['id'] == book_id:
            if request.method == 'GET':
                return jsonify(book), 200

            elif request.method == 'PUT':
                book.update(request.json)
                return jsonify({'message': 'Book updated successfully', 'book': book}), 200

            elif request.method == 'DELETE':
                books.remove(book)
                return jsonify({'message': 'Book deleted successfully'}), 200

    return jsonify({'message': 'Book not found'}), 404
