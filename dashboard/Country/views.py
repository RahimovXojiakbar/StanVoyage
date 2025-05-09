from django.shortcuts import render, redirect
from main import models
from django.contrib import messages



def country_list(request):
    countries = models.Country.objects.filter(is_active=True)

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

def country_edit(request, uuid):
    country = models.Country.objects.get(uuid=uuid)

    if request.method =='POST':
        image = request.FILES.get('image')
        title_en = request.POST.get('title_en')
        title_ru = request.POST.get('title_ru')
        title_fr = request.POST.get('title_fr')
        title_de = request.POST.get('title_de')
        title_es = request.POST.get('title_es')
        description_en = request.POST.get('description_en')
        description_ru = request.POST.get('description_ru')
        description_fr = request.POST.get('description_fr')
        description_de = request.POST.get('description_de')
        description_es = request.POST.get('description_es')

        if image:
            country.image = image
        country.title_en = title_en
        country.title_ru = title_ru
        country.title_fr = title_fr
        country.title_de = title_de
        country.title_es = title_es
        country.description_en = description_en
        country.description_ru = description_ru
        country.description_fr = description_fr
        country.description_de = description_de
        country.description_es = description_es

        country.save()
        messages.success(request, 'Country edited successfully')
        return redirect('country_detail', country.uuid)

def country_delete(request, uuid):
    country = models.Country.objects.get(uuid=uuid)
    if request.method == 'POST':
        country.is_active = False
        country.save()
        messages.success(request, 'Country deleted successfully')
        return redirect('country_list')

def country_create(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        title_en = request.POST.get('title_en')
        description_en = request.POST.get('description_en')

        new_country = models.Country.objects.create(
            image = image, 
            title_en = title_en,
            description_en = description_en
        )
        messages.success(request, 'Country created successfully')
        return redirect('country_detail', new_country.uuid)



# def locations_list(request):
#     locations = models.Locations.filter(is_active=True)

#     context = {
#         locations:'locations'
#     }

#     return render(request, 'locations/list.html', context)


