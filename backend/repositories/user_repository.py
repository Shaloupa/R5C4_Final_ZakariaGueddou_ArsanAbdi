from shared.peristence import load_data, save_data

DATA_PATH = './data/users.json'

def get_all_users():
    return load_data(DATA_PATH)

def get_user_by_id(user_id):
    users = load_data(DATA_PATH)
    return next((u for u in users if u['user_id'] == user_id), None)

def add_user(user_data):
    users = load_data(DATA_PATH)
    user_data['user_id'] = max([u['user_id'] for u in users] + [0]) + 1
    users.append(user_data)
    save_data(DATA_PATH, users)
    return user_data

def update_user(user_id, user_data):
    users = load_data(DATA_PATH)
    user = next((u for u in users if u['user_id'] == user_id), None)
    if user:
        user.update(user_data)
        save_data(DATA_PATH, users)
    return user