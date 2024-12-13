from repositories import satisfaction_repository

def get_all_satisfaction():
    return satisfaction_repository.get_all_satisfaction()

def get_satisfaction_by_message_id(message_id):
    return satisfaction_repository.get_satisfaction_by_message_id(message_id)

def create_satisfaction(satisfaction_data):
    return satisfaction_repository.add_satisfaction(satisfaction_data)

def update_satisfaction(message_id, satisfaction_data):
    return satisfaction_repository.update_satisfaction(message_id, satisfaction_data)