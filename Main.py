import topDestinations
import distanceCalculation
from geopy.geocoders import Nominatim

def getCoordinates(address):
    geolocator = Nominatim(user_agent="TravelRecommendations")

    location = geolocator.geocode(address)

    if location:
        return {'lat': location.latitude, 'lng': location.longitude}
    else:
        return None

def recommendPlaces(destination, start, placesKey, distanceKey, wanted):

    places = topDestinations.getTopDestinations(destination, placesKey, wanted)

    recommendations = []
    for place in places:
        name = place['name']
        location = place['geocodes']['main']

        destinationCoords = {
            'lat': location['latitude'],
            'lng': location['longitude']
        }

        distance = distanceCalculation.getDistance(start, destinationCoords, distanceKey)

        recommendations.append({
            'name': name,
            'address': place.get('location', {}).get('address', 'Address not available'),
            'distance': distance
        })

    return recommendations

startAddress = input("starting address: ")
startCoord = getCoordinates(startAddress)

if not startCoord:
    print("Starting address could not be found.")
else:
    destination = input("wanted destination: ")
    wantedTypePlace = input("pick between musuem, restaurant, bakery, cafe, and bar recs: ")

    placesKey = "fsq3hs55mFSDiRexD5JD1QF5ZZCUUNFR3YEJwTaBw7A9FX4="
    distanceKey = "5b3ce3597851110001cf62484777d740a32d453b8132476b888cf6f0"

    recommendations = recommendPlaces(destination, startCoord, placesKey, distanceKey, wantedTypePlace)
    for rec in recommendations:
        print(f"Place: {rec['name']}, Address: {rec['address']}, Distance: {rec['distance']}")
