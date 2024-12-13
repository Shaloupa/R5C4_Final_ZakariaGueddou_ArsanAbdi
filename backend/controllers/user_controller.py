from flask import Blueprint, jsonify, request, abort
from services import user_service

user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = user_service.get_all_users()
    return jsonify(users)

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user(user_id)
    if user is None:
        abort(404)
    return jsonify(user)

@user_bp.route('/users', methods=['POST'])
def create_user():
    user_data = request.json
    new_user = user_service.create_user(user_data)
    return jsonify(new_user), 201

@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user_data = request.json
    updated_user = user_service.update_user(user_id, user_data)
    if updated_user is None:
        abort(404)
    return jsonify(updated_user)