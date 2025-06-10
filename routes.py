from flask import Blueprint, request, jsonify
from .models import Student
from . import db

main = Blueprint('main', __name__)

# Route to get all students (GET request)
@main.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    result = [{'id': s.id, 'name': s.name, 'email': s.email} for s in students]
    return jsonify(result)

# Route to get a specific student by id (GET request)
@main.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get_or_404(id)
    return jsonify({'id': student.id, 'name': student.name, 'email': student.email})

# Route to create a new student (POST request)
@main.route('/students', methods=['POST'])
def create_student():
    # Get the JSON data from the request
    data = request.get_json()

    # Check if the 'name' and 'email' are present in the request data
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({'error': 'Name and email are required'}), 400

    # Create a new student instance and add to the database
    new_student = Student(name=data['name'], email=data['email'])

    try:
        # Add the new student to the session and commit the transaction
        db.session.add(new_student)
        db.session.commit()

        # Return a success message
        return jsonify({'message': 'Student created successfully', 'student': {'id': new_student.id, 'name': new_student.name, 'email': new_student.email}}), 201
    except Exception as e:
        # Rollback in case of error and return an error message
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route to update a student (PUT request)
@main.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = Student.query.get_or_404(id)
    data = request.get_json()

    # Update the student's name and email
    student.name = data['name']
    student.email = data['email']

    try:
        # Commit the changes to the database
        db.session.commit()
        return jsonify({'message': 'Student updated successfully'}), 200
    except Exception as e:
        
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@main.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    
    try:
    
        db.session.delete(student)
        db.session.commit()
        return jsonify({'message': 'Student deleted successfully'}), 200
    except Exception as e:
    
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
