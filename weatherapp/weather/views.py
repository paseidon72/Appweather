import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm



def index(request):
    appid = '3bbda584e69247bad5b697395941bb33'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

#    form = CityForm()

    cities = City.objects.all()
    all_cities = []
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }
        all_cities.append(city_info)


    context = {'all_info': all_cities}

    return render(request, 'weather/index.html', context)

# Create your views here.
