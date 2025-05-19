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
    locations = models.Locations.objects.filter(country = country, is_active=True)

    context = {
        "country":country,
        "locations":locations
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
        messages.success(request, 'Davlat muvaffaqiyatli yangilandi')
        return redirect('country_detail', country.uuid)

def country_delete(request, uuid):
    country = models.Country.objects.get(uuid=uuid)
    if request.method == 'POST':
        country.is_active = False
        country.save()
        messages.success(request, "Davlat muvaffaqiyatli o'chirildi")
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
        messages.success(request, 'Davlat muvaffaqiyatli yaratildi')
        return redirect('country_detail', new_country.uuid)



def locations_detail(request, uuid):
    locations = models.Locations.objects.get(uuid=uuid)

    context = {
        "locations":locations
    }

    return render(request, 'countries/location_detail.html', context)

def location_edit(request, uuid):
        location = models.Locations.objects.get(uuid=uuid)

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
                location.image = image
            location.title_en = title_en
            location.title_ru = title_ru
            location.title_fr = title_fr
            location.title_de = title_de
            location.title_es = title_es
            location.description_en = description_en
            location.description_ru = description_ru
            location.description_fr = description_fr
            location.description_de = description_de
            location.description_es = description_es

            location.save()
            messages.success(request, 'Joylashuv muvaffaqiyatli yangilandi')
            return redirect('location_detail', location.uuid)

def location_delete(request, uuid):
    location = models.Locations.objects.get(uuid=uuid)
    if request.method == 'POST':
        location.is_active = False
        location.save()
        messages.success(request, 'Joylashuv muvaffaqiyatli o\'chirildi')
        return redirect('country_detail', uuid=location.country.uuid)
        
def location_create(request, uuid):
    country = models.Country.objects.get(uuid=uuid)
    if request.method == 'POST':
        new_location = models.Locations.objects.create(
            country = country,
            image = request.FILES.get("image"),
            title_en = request.POST.get("title_en"),
            description_en = request.POST.get("description_en")
        )
        messages.success(request, "Joylashuv muvaffaqiyatli yaratildi")
        return redirect('location_detail', new_location.uuid)
    
    




def location_images_list(request, uuid):
    location_image = models.LocationImage.objects.filter(uuid=uuid)

    context = {
        "location_image":location_image
    }

    return render(request, "countries/location_image.html", context)

def location_images_create(request, uuid):
    location = models.location