import requests

API_KEY = ""  # You can enter your real API key here later
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    if not API_KEY:
        print(f"Using test data for {city} (no API key)")
        return {
            "name": city,
            "main": {
                "temp": 22.5,
                "humidity": 60
            },
            "weather": [{"description": "clear sky"}],
            "wind": {"speed": 3.5}
        }

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data for {city}: {response.status_code}")
        return None
