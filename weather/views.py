from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


def index(request):
    url = "http://api.weatherapi.com/v1/current.json?key=596cb3327e754baeb07121429230910&q={}&lang=ru"

    cities = City.objects.all()
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    form = CityForm()
    weather_data = []

    for city in cities:
        city_weather = requests.get(url.format(city)).json()
        print(city_weather)

        weather = {
            'city': city_weather['location']['name'],
            'country': city_weather['location']['country'],
            'condition': city_weather['current']['condition']['text'],
            'temp': round(int(city_weather['current']['temp_c']), 0),
        }
        weather_data.append(weather)

    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'index.html', context)
