from flask import Blueprint, jsonify, request, abort
from services import satisfaction_service

satisfaction_bp = Blueprint('satisfaction', __name__)

@satisfaction_bp.route('/satisfaction', methods=['GET'])
def get_all_satisfaction():
    satisfaction_data = satisfaction_service.get_all_satisfaction()
    return jsonify(satisfaction_data)

@satisfaction_bp.route('/satisfaction/<int:message_id>', methods=['GET'])
def get_satisfaction(message_id):
    entry = satisfaction_service.get_satisfaction_by_message_id(message_id)
    if entry is None:
        abort(404)
    return jsonify(entry)

@satisfaction_bp.route('/satisfaction', methods=['POST'])
def create_satisfaction():
    satisfaction_data = request.json
    new_entry = satisfaction_service.create_satisfaction(satisfaction_data)
    return jsonify(new_entry), 201

@satisfaction_bp.route('/satisfaction/<int:message_id>', methods=['PUT'])
def update_satisfaction(message_id):
    satisfaction_data = request.json
    updated_entry = satisfaction_service.update_satisfaction(message_id, satisfaction_data)
    if updated_entry is None:
        abort(404)
    return jsonify(updated_entry)