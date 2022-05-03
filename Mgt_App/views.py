from django.shortcuts import render
import requests
from .models import *

# Create your views here.

def future(request):
    url = 'http://api.weatherapi.com/v1/forecast.json?key=22ace5ac6ed74aa397c195726220105&q={}&days=2&aqi=no&alerts=no'

    region = 'Turkana'

    region_data = []
    # for region in regions:

    response = requests.get(url.format(region))
    # print(response.text)
    r = response.json()
    general = {
        'country': r['location']['country'],
        'name':r['location']['name'],
        'city' : r ['location']['region'],
        'latitude':r['location']['lat'] ,
        'longitude':r['location']['lon'] ,
        'condition' : r['current']['condition']['text'],
        'image' : r['current']['condition']['icon'],
    }

    forecast = r['forecast']['forecastday']
    # print(forecast)
    region_data.append(general)
    print(region_data)

    return render(request,'future.html',{"general":general,"forecast":forecast})