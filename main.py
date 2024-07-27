import tkinter as tk
from ui_interaction import WeatherApp
from settings import load_settings, save_settings

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    
    
    settings = load_settings()
    app.units = settings.get('units', 'metric')
    
    
    def on_exit():
        settings = {
            'units': app.units,
        }
        save_settings(settings)
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_exit)
    root.mainloop()
