import requests

def placeToCategoryID(wanted):
    if wanted.lower() == "museum":
        return "4bf58dd8d48988d181941735"
    if wanted.lower() == "restaurant":
        return "4d4b7105d754a06374d5c5c5"
    if wanted.lower() == "bakery":
        return "4bf58dd8d48988d1c9441735"
    if wanted.lower() == "cafe":
        return "4bf58dd8d48988d1e2931735"
    if wanted.lower() == "bar":
        return "4bf58dd8d48988d1c894f3c5"

def getTopDestinations(destination, apiKey, wanted):
    categoryID = placeToCategoryID(wanted)

    url = url = "https://api.foursquare.com/v3/places/search"
    headers = {
        "Accept": "application/json",
        "Authorization": apiKey
    }

    params = {
        "categories": categoryID,
        "near": destination,
        "limit": 10,
        "sort": "relevance"
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        # Return the list of places
        return response.json().get("results", [])
    else:
        print("Error:", response.json())
        return []