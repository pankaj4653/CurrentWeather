from django.shortcuts import render
import requests
from . forms import cityform
from django.http import HttpResponse
from .models import AddCity
# Create your views here.

url ='http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=f8dbb5537ce17da31eddd5a350c479f5'

def index(request):
        if(request.method == "POST"):
                form = cityform(request.POST)
                if form.is_valid():
                    form.save()

                cities = AddCity.objects.all()
                citylist=list()

                for city in cities:
                        r = requests.get(url.format(city.cityName))
                        r_dict = r.json()
                        dict = {
                                    'city' : city,
                                    'temp' : r_dict['main']['temp'], 
                                    'description' : r_dict['weather'][0]['description'],
                                    'icon' : r_dict['weather'][0]['icon']
                                }
                        citylist.append(dict)
                return render(request, 'weather/weather.html',{'citylist':citylist,'form':form})
        else:
            form = cityform()
        return render(request, 'weather/weather.html',{'form':form})



def home(request):
    return HttpResponse(request.method)