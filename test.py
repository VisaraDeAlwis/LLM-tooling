from temperature import get_weather
from location import get_city_coordinates, get_near_fuelStations
from dotenv import load_dotenv
import os

load_dotenv()

api_key_temp = os.getenv("API_KEY_TEMP")
api_key_location = os.getenv("API_KEY_LOCATION")

cities = ['Matugama', 'Colombo', 'Bandarawela']
town = "Matugama"

# 🔸 Show weather for each city
for city in cities:
    weather = get_weather(city, api_key_temp)
    if "error" in weather:
        print("Error:", weather["error"])
    else:
        print(f"\n📍 City: {weather['location']}")
        print(f"🌡️ Temperature: {weather['temperature']}°C")
        print(f"🌤️ Condition: {weather['condition'].capitalize()}")

# 🔸 Show fuel stations near `town`
print(f"\n⛽ Fuel Stations Near {town}:\n" + "-"*40)
fuel_stations = get_near_fuelStations(town, api_key_location)

if isinstance(fuel_stations, dict) and "error" in fuel_stations:
    print("Error:", fuel_stations["error"])
elif isinstance(fuel_stations, dict) and "message" in fuel_stations:
    print(fuel_stations["message"])
else:
    for i, station in enumerate(fuel_stations, start=1):
        print(f"{i}. 🏪 Name   : {station['name']}")
        print(f"   📍 Address: {station.get('address', 'N/A')}")
        print(f"   ⭐ Rating : {station.get('rating', 'N/A')}\n")
