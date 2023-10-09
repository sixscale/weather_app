from django.shortcuts import render
import requests


def index(request):
    url = "http://api.weatherapi.com/v1/current.json?key=596cb3327e754baeb07121429230910&q=Москва&lang=ru"

    city = 'Moscow'
    city_weather = requests.get(url.format(city)).json()

    print(city_weather)

    weather = {
        'city': city_weather['location']['name'],
        'condition': city_weather['current']['condition']['text'],
        'temp': round(int(city_weather['current']['temp_c']), 0),
        #'temp': city_weather['current']['condition']['temp_c']
    }

    context = {'weather': weather}
    return render(request, 'index.html', context)
