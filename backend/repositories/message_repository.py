from shared.peristence import load_data, save_data

DATA_PATH = './data/messages.json'

def get_all_messages():
    return load_data(DATA_PATH)

def get_message_by_id(message_id):
    messages = load_data(DATA_PATH)
    return next((m for m in messages if m['message_id'] == message_id), None)

def add_message(message_data):
    messages = load_data(DATA_PATH)
    message_data['message_id'] = max([m['message_id'] for m in messages] + [0]) + 1
    messages.append(message_data)
    save_data(DATA_PATH, messages)
    return message_data

def update_message(message_id, message_data):
    messages = load_data(DATA_PATH)
    message = next((m for m in messages if m['message_id'] == message_id), None)
    if message:
        message.update(message_data)
        save_data(DATA_PATH, messages)
    return message