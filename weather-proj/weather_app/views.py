from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import crawler
import pandas as pd

# Create your views here.
def index(request):
    cities = ['New York', 'London', 'Tokyo', 'Beijing']
    resultJson = [crawler.current(city) for city in cities]
    return render(request, 'index.html', {'weathers': resultJson, })

@csrf_exempt
def forecast(request):
    city = request.POST.get('cityName')
    resultJson = crawler.forecast(city)

    return render(request, 'search.html', {'weathers': resultJson})