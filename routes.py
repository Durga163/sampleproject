from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pushups.db'
db = SQLAlchemy(app)

@app.route('/', methods=['GET'])
def home():
    return "Welcome to Push-Up Logger API"

@app.route('/pushups', methods=['POST'])
def log_pushups():
    data = request.get_json()
    # Handle data saving here
    return jsonify({'message': 'Push-up logged successfully'})
