from shared.peristence import load_data, save_data

DATA_PATH = './data/conversations.json'

def get_all_conversations():
    return load_data(DATA_PATH)

def get_conversation_by_id(conversation_id):
    conversations = load_data(DATA_PATH)
    return next((c for c in conversations if c['conversation_id'] == conversation_id), None)

def add_conversation(conversation_data):
    conversations = load_data(DATA_PATH)
    conversation_data['conversation_id'] = max([c['conversation_id'] for c in conversations] + [0]) + 1
    conversations.append(conversation_data)
    save_data(DATA_PATH, conversations)
    return conversation_data

def update_conversation(conversation_id, conversation_data):
    conversations = load_data(DATA_PATH)
    conversation = next((c for c in conversations if c['conversation_id'] == conversation_id), None)
    if conversation:
        conversation.update(conversation_data)
        save_data(DATA_PATH, conversations)
    return conversation