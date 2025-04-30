import json

def save_weather_to_file(city, data):
    filename = f"{city.lower().replace(' ', '_')}_weather.json"
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def log_summary(city, data):
    with open("weather_summary.txt", "a") as f:
        summary = f"{city}: {data['main']['temp']}°C, {data['weather'][0]['description']}, Humidity: {data['main']['humidity']}%, Wind: {data['wind']['speed']} m/s\n"
        f.write(summary)
