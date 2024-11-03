import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def getDistance(start, destinationCoord, apiKey):
    url = "https://api.openrouteservice.org/v2/matrix/driving-car"
    headers = {
        "Authorization": apiKey,
        "Content-Type": "application/json"
    }
    body = {
        "locations": [
            [start['lng'], start['lat']],
            [destinationCoord['lng'], destinationCoord['lat']]
        ],
        "metrics": ["distance"]
    }

    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
    session.mount('https://', HTTPAdapter(max_retries=retries))

    try:
        response = session.post(url, headers=headers, json=body)
        response.raise_for_status()

        distance_meters = response.json()["distances"][0][1]
        return f"{distance_meters / 1000:.2f} km"
    except requests.exceptions.RequestException as e:
        print("Error with OpenRouteService API request:", e)
        return "N/A"
