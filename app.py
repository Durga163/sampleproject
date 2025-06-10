from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///green_street.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize DB
db = SQLAlchemy(app)

# Model
class Tree(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    species = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)

# Routes
@app.route('/')
def home():
    return {"message": "Welcome to Green Street API"}

@app.route('/trees', methods=['GET'])
def get_trees():
    trees = Tree.query.all()
    return jsonify([{"id": t.id, "species": t.species, "location": t.location, "age": t.age} for t in trees])

@app.route('/trees', methods=['POST'])
def add_tree():
    data = request.get_json()
    new_tree = Tree(
        species=data['species'],
        location=data['location'],
        age=data.get('age')
    )
    db.session.add(new_tree)
    db.session.commit()
    return jsonify({"message": "Tree added successfully!"}), 201

@app.route('/trees/<int:id>', methods=['DELETE'])
def delete_tree(id):
    tree = Tree.query.get_or_404(id)
    db.session.delete(tree)
    db.session.commit()
    return jsonify({"message": "Tree deleted successfully!"})

# Main
if __name__ == '__main__':
    app.run(debug=True)
=======
from flask import Flask, request, jsonify, render_template
import json
import os
from datetime import datetime  # Fixed typo in 'datetime'

app = Flask(__name__)

DATA_DIR = 'data'
BOOKS_FILE = os.path.join(DATA_DIR, 'books.json')  # Fixed 'os.path.json' -> 'os.path.join'
STUDENT_FILE = os.path.join(DATA_DIR, 'students.json')  # Fixed 'DATA_DIR' typo

# Function to load data
def load_data(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:  # Fixed 'a file' -> 'file'
            return json.load(file)
    return []  # Fixed incorrect return inside 'if'

# Function to save data
def save_data(filename, data):  
    with open(filename, 'w') as file:  # Fixed 'a file' -> 'file'
        json.dump(data, file, indent=4)  # Added indentation for readability

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/books', methods=['GET'])  # Fixed missing '/'
def get_books():
    books = load_data(BOOKS_FILE)  # Corrected 'students' -> 'books'
    return jsonify(books)

@app.route('/add_book', methods=['POST'])
def add_book():
    book = request.json
    books = load_data(BOOKS_FILE)

    # Add the new book with status 'available'
    book["status"] = "available"
    books.append(book)

    save_data(BOOKS_FILE, books)
    return jsonify({"message": "Book added successfully", "book": book}), 201

if __name__ == '__main__':
    os.makedirs(DATA_DIR, exist_ok=True)  # Ensure 'data' directory exists
    app.run(debug=True)

