from django.shortcuts import render
import requests

# Create your views here.

def future(request):
    url = 'http://api.weatherapi.com/v1/forecast.json?key=22ace5ac6ed74aa397c195726220105&q=London&days=10&aqi=no&alerts=no'

    response = requests.get(url)
    # print(response.text)
    r = response.json()
    general = {
        'country': r['location']['country'],
        'city' : r ['location']['region'],
        'latitude':r['location']['lat'] ,
        'longitude':r['location']['lon'] ,
        'condition' : r['current']['condition']['text'],
        'image' : r['current']['condition']['icon'],
    }
    forecast = {
        'Average Temperature in Celsius':r['forecast']['forecastday'][0]['day']['avgtemp_c'] ,
        'Total Rainfall in mm':r['forecast']['forecastday'][0]['day']['totalprecip_mm'] ,
        'Average Humidity': r['forecast']['forecastday'][0]['day']['avghumidity'] ,
    }

    # print(forecast)

    return render(request,'future.html',{"general":general,"forecast":forecast})