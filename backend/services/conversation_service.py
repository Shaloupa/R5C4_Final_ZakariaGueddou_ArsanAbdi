from repositories import conversation_repository

def get_all_conversations():
    return conversation_repository.get_all_conversations()

def get_conversation(conversation_id):
    return conversation_repository.get_conversation_by_id(conversation_id)

def create_conversation(conversation_data):
    return conversation_repository.add_conversation(conversation_data)

def update_conversation(conversation_id, conversation_data):
    return conversation_repository.update_conversation(conversation_id, conversation_data)