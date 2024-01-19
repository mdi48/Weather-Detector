from django.shortcuts import render
import json, os
import urllib.request
from weatherdetector.settings import OPENWEATHERMAP_API_KEY

#OPENWEATHERMAP_API_KEY = os.environ.get('OPENWEATHERMAP_API_KEY')

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        if ' ' in city:
            city = city.replace(' ', '+')
        res = urllib.request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERMAP_API_KEY}').read()
        json_data = json.loads(res)
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' +
                str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp']) + 'k',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }
        city = city.replace('+', ' ')

    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city': city, 'data': data})
