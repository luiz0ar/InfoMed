from flask import Blueprint, request, jsonify
from app.models import User
from app import db

main_routes = Blueprint('main', __name__)

@main_routes.route('/register', methods=['POST'])
def register_user():
    data = request.json
    user = User(
        name=data['name'],
        age=data['age'],
        weight=data['weight'],
        height=data['height'],
        city=data['city'],
        allergies=data.get('allergies'),
        chronic_diseases=data.get('chronic_diseases'),
        medications=data.get('medications'),
        family_history=data.get('family_history')
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered successfully!"}), 201
