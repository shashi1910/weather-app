import requests
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_URL = 'http://api.openweathermap.org/data/2.5/'

def fetch_current_weather(location):
    url = f"{BASE_URL}weather?q={location}&appid={API_KEY}"
    response = requests.get(url)
    try:
        response_data = response.json()
    except ValueError:
        response_data = {}
    return response_data

def fetch_weather_forecast(location, days=5):
    url = f"{BASE_URL}forecast/daily?q={location}&cnt={days}&appid={API_KEY}"
    response = requests.get(url)
    try:
        response_data = response.json()
    except ValueError:
        response_data = {}
    return response_data

def fetch_historical_weather(location, date):
    timestamp = int(datetime.strptime(date, "%Y-%m-%d").timestamp())
    url = f"{BASE_URL}timemachine?location={location}&dt={timestamp}&appid={API_KEY}"
    response = requests.get(url)
    try:
        response_data = response.json()
    except ValueError:
        response_data = {}
    return response_data

def convert_units(data, units='metric'):
    if units == 'metric':
        # Convert into metric units
        pass
    elif units == 'imperial':
        # Convert into imperial units
        pass
    return data
