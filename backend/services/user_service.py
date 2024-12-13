from repositories import user_repository

def get_all_users():
    return user_repository.get_all_users()

def get_user(user_id):
    return user_repository.get_user_by_id(user_id)

def create_user(user_data):
    return user_repository.add_user(user_data)

def update_user(user_id, user_data):
    return user_repository.update_user(user_id, user_data)