from secrets_1 import api_key
import requests
import json

URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = api_key
CITY = "Viksjö, SE"

url = URL + "appid" + API_KEY + "&q=" + CITY

response = requests.get(url).json()

print(response)
