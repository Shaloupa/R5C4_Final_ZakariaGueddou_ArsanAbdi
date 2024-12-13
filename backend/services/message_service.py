from repositories import message_repository

def get_all_messages():
    return message_repository.get_all_messages()

def get_message(message_id):
    return message_repository.get_message_by_id(message_id)

def create_message(message_data):
    return message_repository.add_message(message_data)

def update_message(message_id, message_data):
    return message_repository.update_message(message_id, message_data)