from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

# Create your views here.
def index(request):
    # url = 'http://api.weatherapi.com/v1/current.json?key=32a3b01ce8c24f0c8fb100757220205&q=London&aqi=no'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=4bd83fccf0cdcfdb590368fea0c32db2'
    weather_data = []

    cities = City.objects.all() 
   
    
    # for city in cities:
    #     city_weather = requests.get(url).json() #request the API data and convert the JSON to Python data types
    #     print(city_weather)
    #     weather = {
    #         'city' : city_weather['location']['name'],
    #         'temperature' : city_weather['current']['temp_c'],
            
    #     }
    #     weather_data.append(weather) 
    # print(weather)
    for city in cities:

        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon'],
            'country':city_weather['sys']['country']
        }

        weather_data.append(weather) #add the data for the current city into our list

    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
       
        form.save() 
    form = CityForm()
    context = {'weather_data' : weather_data, 'form' : form}
        
    return render (request,'index.html',context)
