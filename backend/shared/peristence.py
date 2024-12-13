import json
import os

def load_data(path):
    with open(path, 'r') as file:
        return json.load(file)

def save_data(path, data):
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)