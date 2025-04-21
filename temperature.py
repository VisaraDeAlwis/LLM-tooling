import requests

def get_weather(city_name, api_key):
  
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric" 
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise error for HTTP codes
        data = response.json()

        weather_info = {
            "location": data["name"],
            "temperature": data["main"]["temp"],
            "condition": data["weather"][0]["description"]
        }
        return weather_info

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
    except KeyError:
        return {"error": "Could not parse weather data."}
