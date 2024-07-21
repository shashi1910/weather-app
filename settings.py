import json

def load_settings():
    try:
        with open('settings.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {'units': 'metric', 'notifications': True}

def save_settings(settings):
    with open('settings.json', 'w') as file:
        json.dump(settings, file)
