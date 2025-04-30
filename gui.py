import tkinter as tk
from weather_api import get_weather
from file_manager import save_weather_to_file, log_summary

def launch_app():
    def fetch_weather():
        city = city_entry.get()
        data = get_weather(city)
        if data:
            save_weather_to_file(city, data)
            log_summary(city, data)
            temp_f = data['main']['temp'] * 9/5 + 32
            desc = data['weather'][0]['description']
            result = f"{city}: {temp_f:.1f}°F, {desc}"
        else:
            result = "Could not get weather."
        result_label.config(text=result)

    root = tk.Tk()
    root.title("Weather Checker")

    tk.Label(root, text="Enter city name:").pack()
    city_entry = tk.Entry(root)
    city_entry.pack()

    tk.Button(root, text="Get Weather", command=fetch_weather).pack()

    result_label = tk.Label(root, text="")
    result_label.pack()

    root.mainloop()

# Start the GUI
launch_app()
