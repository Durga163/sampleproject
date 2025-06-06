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
