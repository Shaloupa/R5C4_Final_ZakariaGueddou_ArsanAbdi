from shared.peristence import load_data, save_data

DATA_PATH = './data/satisfaction.json'

def get_all_satisfaction():
    return load_data(DATA_PATH)

def get_satisfaction_by_message_id(message_id):
    satisfaction_data = load_data(DATA_PATH)
    return next((s for s in satisfaction_data if s['message_id'] == message_id), None)

def add_satisfaction(satisfaction_data):
    satisfaction_entries = load_data(DATA_PATH)
    satisfaction_entries.append(satisfaction_data)
    save_data(DATA_PATH, satisfaction_entries)
    return satisfaction_data

def update_satisfaction(message_id, satisfaction_data):
    satisfaction_entries = load_data(DATA_PATH)
    entry = next((s for s in satisfaction_entries if s['message_id'] == message_id), None)
    if entry:
        entry.update(satisfaction_data)
        save_data(DATA_PATH, satisfaction_entries)
    return entry