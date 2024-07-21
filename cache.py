import time

CACHE = {}

def cache_weather_data(location, data, expiration=3600):
    CACHE[location] = {
        'data': data,
        'expiration': time.time() + expiration
    }

def get_cached_weather_data(location):
    if location in CACHE:
        if CACHE[location]['expiration'] > time.time():
            return CACHE[location]['data']
        else:
            del CACHE[location]
    return None
