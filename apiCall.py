import requests
import geocoder
from key import key


my_location= geocoder.ip('me')
latitude= my_location.geojson['features'][0]['properties']['lat']
longitude = my_location.geojson['features'][0]['properties']['lng']

#get the location
print("Your Current IP location is: Longitude",longitude," and Latitude: ", latitude)
res = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (latitude, longitude, key))
print(res)