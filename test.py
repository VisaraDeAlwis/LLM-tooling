from temperature import get_weather
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

list=['Matugama', 'Colombo','Bandarawela']

for city in list:
        weather = get_weather(city, api_key)
        if "error" in weather:
            print("Error:", weather["error"])
        else:
            print(f"📍 {weather['location']}")
            print(f"🌡️ Temperature: {weather['temperature']}°C")
            print(f"🌤️ Condition: {weather['condition'].capitalize()}")