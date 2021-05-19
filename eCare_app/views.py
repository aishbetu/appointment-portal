from django.shortcuts import render
from .models import CaraouselData
import requests
# Create your views here.

def covid_data(request):
    api_response = requests.get('https://covid19.mathdro.id/api/countries/india')
    covid_data = (api_response.json())
    trim_last_update = covid_data['lastUpdate']
    trimmed_date = trim_last_update.find('T') # Here I'm trimming date_time string to show only date. T was for time to I split till T and store prior string
    res_trimmed_date = trim_last_update[:trimmed_date] # This will print string till T but not T and afterwards
    confirmed = covid_data['confirmed']
    recovered = covid_data['recovered']
    deaths = covid_data['deaths']
    context = {
        'res_trimmed_date': res_trimmed_date,
        'confirmed': confirmed['value'],
        'recovered': recovered['value'],
        'deaths': deaths['value']
    }
    return context

def home(request):
    caraousel_data = CaraouselData.objects.all()
    for item in caraousel_data:
        print(item.image)
    data = covid_data(request)
    return render(request, 'index.html', context={
        'confirmed': data['confirmed'],
        'recovered': data['recovered'],
        'deaths': data['deaths'],
        'res_trimmed_date': data['res_trimmed_date'],
        'caraousel_data': caraousel_data,
    })

# whats new section
def update(request):
    return render(request, 'update.html')


def tutorial(request):
    return render(request, 'tutorial.html')


def about_us(request):
    return render(request, 'about.html')

def contact_us(request):
    return render(request, 'contact.html')