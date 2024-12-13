from flask import Blueprint, jsonify, request, abort
from services import message_service

message_bp = Blueprint('message', __name__)

@message_bp.route('/messages', methods=['GET'])
def get_messages():
    messages = message_service.get_all_messages()
    return jsonify(messages)

@message_bp.route('/messages/<int:message_id>', methods=['GET'])
def get_message(message_id):
    message = message_service.get_message(message_id)
    if message is None:
        abort(404)
    return jsonify(message)

@message_bp.route('/messages', methods=['POST'])
def create_message():
    message_data = request.json
    new_message = message_service.create_message(message_data)
    return jsonify(new_message), 201

@message_bp.route('/messages/<int:message_id>', methods=['PUT'])
def update_message(message_id):
    message_data = request.json
    updated_message = message_service.update_message(message_id, message_data)
    if updated_message is None:
        abort(404)
    return jsonify(updated_message)