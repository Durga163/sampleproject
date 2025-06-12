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
