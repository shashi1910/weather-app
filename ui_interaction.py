import tkinter as tk
from tkinter import ttk
import json  
from data_retrieval import fetch_current_weather, fetch_weather_forecast
from utils import format_weather_data
from cache import cache_weather_data, get_cached_weather_data

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        self.units = 'metric'
        
        self.location_entry = ttk.Entry(root, width=30)
        self.location_entry.grid(row=0, column=0, padx=10, pady=10)
        
        self.search_button = ttk.Button(root, text="Search", command=self.search_location)
        self.search_button.grid(row=0, column=1, padx=10, pady=10)
        
        self.weather_display = tk.Text(root, width=50, height=10)
        self.weather_display.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        
        self.settings_button = ttk.Button(root, text="Settings", command=self.settings_menu)
        self.settings_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def display_current_weather(self, weather_data):
        self.weather_display.delete(1.0, tk.END)
        formatted_data = format_weather_data(weather_data, self.units)
        self.weather_display.insert(tk.END, formatted_data)

    def search_location(self):
        location = self.location_entry.get()
        cached_data = get_cached_weather_data(location)
        if cached_data:
            self.display_current_weather(cached_data)
        else:
            weather_data = fetch_current_weather(location)
            if weather_data.get('cod') != 200:
                self.weather_display.delete(1.0, tk.END)
                self.weather_display.insert(tk.END, f"Error: {weather_data.get('message', 'Unknown error')}")
            else:
                cache_weather_data(location, weather_data)
                self.display_current_weather(weather_data)

    def settings_menu(self):
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Settings")
        
        unit_label = ttk.Label(settings_window, text="Units:")
        unit_label.grid(row=0, column=0, padx=10, pady=10)
        
        unit_var = tk.StringVar(value=self.units)
        unit_metric = ttk.Radiobutton(settings_window, text="Metric", variable=unit_var, value='metric')
        unit_imperial = ttk.Radiobutton(settings_window, text="Imperial", variable=unit_var, value='imperial')
        unit_metric.grid(row=0, column=1, padx=10, pady=10)
        unit_imperial.grid(row=0, column=2, padx=10, pady=10)
        
        def save_settings():
            self.units = unit_var.get()
            settings_window.destroy()
        
        save_button = ttk.Button(settings_window, text="Save", command=save_settings)
        save_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    def show_weather_alerts(self, alerts):
        self.weather_display.delete(1.0, tk.END)
        self.weather_display.insert(tk.END, json.dumps(alerts, indent=2))
