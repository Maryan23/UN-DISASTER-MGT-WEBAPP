from django.shortcuts import render
import requests

# Create your views here.

def future(request):
    url = 'http://api.weatherapi.com/v1/current.json?key=22ace5ac6ed74aa397c195726220105&q=Nairobi&aqi=no'
    city = 'Nairobi'

    response = requests.get(url)
    print(response.text)
    r = response.json()
    return render(request,'future.html',{"r":r})