import requests
import geocoder
from key import key
import json

my_location= geocoder.ip('me')
latitude= my_location.geojson['features'][0]['properties']['lat']
longitude = my_location.geojson['features'][0]['properties']['lng']

#get the location
print("Your Current IP location is: Longitude",longitude," and Latitude: ", latitude)
res = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (latitude, longitude, key))

data = json.loads(res.text)
current_weather = data['current']


temp = current_weather['temp']
humd = current_weather['humidity']

weat = current_weather['weather'][0]
weat_main =  weat['main']
weat_desc =  weat['description']

city = my_location.geojson['features'][0]['properties']['city']
country = my_location.geojson['features'][0]['properties']['country']

print("For ", city,country,"the temperature is ",temp,"C")
print("The weather is ", weat_main," with ",weat_desc)
print("The humidity is ",humd,"%")