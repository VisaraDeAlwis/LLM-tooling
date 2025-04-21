import requests

def get_city_coordinates(city_name, api_key):

    geo_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": city_name,
        "key": api_key
    }
    response = requests.get(geo_url, params=params)
    response.raise_for_status()
    data = response.json()

    if data["status"] == "OK":
        location = data["results"][0]["geometry"]["location"]
        return location["lat"], location["lng"]
    else:
        raise Exception(f"Geocoding failed: {data.get('status')}")

def get_near_fuelStations(city_name, api_key):

    try:
        # Step 1: Get coordinates
        lat, lng = get_city_coordinates(city_name, api_key)

        # Step 2: Call Places API
        places_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        params = {
            "location": f"{lat},{lng}",
            "radius": 5000,
            "type": "gas_station",
            "key": api_key
        }
        response = requests.get(places_url, params=params)
        response.raise_for_status()
        data = response.json()


        stations = []
        for place in data.get("results", []):
            stations.append({
                "name": place["name"],
                "address": place.get("vicinity"),
                "rating": place.get("rating", "N/A")
            })

        return stations if stations else {"message": "No fuel stations found."}

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": str(e)}
