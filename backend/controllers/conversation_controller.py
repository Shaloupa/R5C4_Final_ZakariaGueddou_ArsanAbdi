from flask import Blueprint, jsonify, request, abort
from services import conversation_service

conversation_bp = Blueprint('conversation', __name__)

@conversation_bp.route('/conversations', methods=['GET'])
def get_conversations():
    conversations = conversation_service.get_all_conversations()
    return jsonify(conversations)

@conversation_bp.route('/conversations/<int:conversation_id>', methods=['GET'])
def get_conversation(conversation_id):
    conversation = conversation_service.get_conversation(conversation_id)
    if conversation is None:
        abort(404)
    return jsonify(conversation)

@conversation_bp.route('/conversations', methods=['POST'])
def create_conversation():
    conversation_data = request.json
    new_conversation = conversation_service.create_conversation(conversation_data)
    return jsonify(new_conversation), 201

@conversation_bp.route('/conversations/<int:conversation_id>', methods=['PUT'])
def update_conversation(conversation_id):
    conversation_data = request.json
    updated_conversation = conversation_service.update_conversation(conversation_id, conversation_data)
    if updated_conversation is None:
        abort(404)
    return jsonify(updated_conversation)