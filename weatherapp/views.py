import requests
import datetime
from django.shortcuts import render

def home(request):
    # If user enters a city manually, use it — otherwise default to Bengaluru
    city = request.POST.get('city', 'Bengaluru')

    api_key = 'cbb909d7aab4ceb89074fe19cdd9d61d'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    params = {'units': 'metric'}

    data = requests.get(url, params=params).json()
    print(data)  # Debugging

    # Handle errors like wrong city name
    if data.get("cod") != 200:
        return render(request, 'weatherapp/index.html', {
            'error': data.get("message", "Unable to fetch weather data"),
            'city': city
        })

    # Extract weather info
    context = {
        'description': data['weather'][0]['description'],
        'icon': data['weather'][0]['icon'],
        'temp': data['main']['temp'],
        'day': datetime.date.today(),
        'city': city
    }

    return render(request, 'weatherapp/index.html', context)