from django.shortcuts import render
from main import models

def country_list(request):
    countries = models.Country.objects.filter()

    context = {
        "countries":countries
    }

    return render(request, 'countries/list.html', context)

def country_detail(request, uuid):
    country = models.Country.objects.get(uuid=uuid)

    context = {
        "country":country
    }

    return render(request, 'countries/detail.html', context)

# def locations_list(request):
#     locations = models.Locations.filter(is_active=True)

#     context = {
#         locations:'locations'
#     }

#     return render(request, 'locations/list.html', context)
