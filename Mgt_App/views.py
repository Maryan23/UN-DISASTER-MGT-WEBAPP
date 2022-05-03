from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

# Create your views here.
def index(request):
    url = 'http://api.weatherapi.com/v1/current.json?key=32a3b01ce8c24f0c8fb100757220205 &q=London&aqi=no'
    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() 
    form = CityForm()
    weather_data = []

    cities = City.objects.all() 
    context = {'weather_data' : weather_data, 'form' : form}
    
    for city in cities:
        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
        print(city_weather)
        weather = {
            'city' : city['location']['name'],
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }
        weather_data.append(weather) 

   
        
    return render (request,'index.html',context)
