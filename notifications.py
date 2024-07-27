import time
import threading
from data_retrieval import fetch_current_weather
from cache import cache_weather_data

def send_weather_notification(weather_data):
    
    pass

def update_weather_in_background(location):
    while True:
        weather_data = fetch_current_weather(location)
        cache_weather_data(weather_data)
        time.sleep(3600)  

def schedule_daily_forecast_notification(location, time_of_day):
    
    pass

def check_weather_conditions_for_activities(location, activity):
    weather_data = fetch_current_weather(location)
    
    return True

def monitor_location_changes():
    
    pass


background_thread = threading.Thread(target=update_weather_in_background, args=("New York",))
background_thread.start()
