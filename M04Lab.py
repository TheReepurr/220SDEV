from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory "database" (dictionary to store books)
books = {}
next_id = 1

# Create (POST)
@app.route('/books', methods=['POST'])
def create_book():
    global next_id
    data = request.get_json()
    
    # Validate the required fields
    if not all(key in data for key in ("book_name", "author", "publisher")):
        return jsonify({"error": "Missing required fields"}), 400

    book = {
        "id": next_id,
        "book_name": data["book_name"],
        "author": data["author"],
        "publisher": data["publisher"]
    }
    books[next_id] = book
    next_id += 1

    return jsonify(book), 201

# Read all books (GET)
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(list(books.values())), 200

# Read a single book (GET)
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = books.get(book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book), 200

# Update (PUT)
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = books.get(book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404

    data = request.get_json()
    book["book_name"] = data.get("book_name", book["book_name"])
    book["author"] = data.get("author", book["author"])
    book["publisher"] = data.get("publisher", book["publisher"])
    books[book_id] = book

    return jsonify(book), 200

# Delete (DELETE)
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = books.pop(book_id, None)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    return jsonify({"message": "Book deleted successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)
