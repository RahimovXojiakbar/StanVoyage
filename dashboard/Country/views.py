from django.shortcuts import render, redirect
from main import models
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def country_list(request):
    countries = models.Country.objects.filter(is_active=True)

    context = {
        "countries":countries
    }

    return render(request, 'countries/list.html', context)

@login_required(login_url='login')
def country_detail(request, uuid):
    country = models.Country.objects.get(uuid=uuid)
    locations = models.Locations.objects.filter(country = country, is_active=True)

    context = {
        "country":country,
        "locations":locations
    }

    return render(request, 'countries/detail.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
def country_delete(request, uuid):
    country = models.Country.objects.get(uuid=uuid)
    if request.method == 'POST':
        country.is_active = False
        country.save()
        messages.success(request, "Davlat muvaffaqiyatli o'chirildi")
        return redirect('country_list')

@login_required(login_url='login')
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


@login_required(login_url='login')
def locations_detail(request, uuid):
    locations = models.Locations.objects.get(uuid=uuid)
    location_images = models.LocationImage.objects.filter(location = locations, is_active=True)

    context = {
        "locations":locations,
        "location_images":location_images

    }
    

    return render(request, 'countries/location_detail.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
def location_delete(request, uuid):
    location = models.Locations.objects.get(uuid=uuid)
    if request.method == 'POST':
        location.is_active = False
        location.save()
        messages.success(request, 'Joylashuv muvaffaqiyatli o\'chirildi')
        return redirect('country_detail', uuid=location.country.uuid)
        
@login_required(login_url='login')
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
    
@login_required(login_url='login')
def location_image_create(request, uuid):
    location = models.Locations.objects.get(uuid=uuid)
    if request.method == 'POST':
        image = request.FILES.get('image')
        
        new_location_image = models.LocationImage.objects.create(
            location = location,
            image=image
        )
        messages.success(request, 'Joylashuv rasmi muvaffaqiyatli yaratildi!')
        return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='login')
def location_image_edit(request, uuid):
    location_image = models.LocationImage.objects.get(uuid=uuid)
    image = request.FILES.get('image')
    
    if request.method == 'POST':
        if image:
            location_image.image = image
        
        location_image.save()
        messages.success(request, 'Sayohat rasmi muvaffaqiyatli yangilandi!')
        return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='login')
def location_image_delete(request, uuid):
    location_image = models.LocationImage.objects.get(uuid=uuid)
    if request.method == 'POST':
        location_image.is_active = False
        location_image.save()
        messages.success(request, 'Sayohat rasmi muvaffaqiyatli o\'chirildi!')
        return redirect(request.META.get('HTTP_REFERER'))
