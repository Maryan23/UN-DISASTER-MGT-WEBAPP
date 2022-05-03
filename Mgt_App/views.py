from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    url = 'http://api.weatherapi.com/v1/current.json?key=32a3b01ce8c24f0c8fb100757220205 &q=London&aqi=no'

    city = 'Las Vegas'

    city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

    print(city_weather)
    return render(request,'index.html')
