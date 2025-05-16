from django.shortcuts import render, redirect
from main import models
from django.contrib import messages

def trip_list(request):
    trips = models.Trip.objects.filter(is_active=True)

    context = {
        "trips":trips
    }

    return render(request, 'trips/list.html', context)

def trip_detail(request, uuid):
    trip = models.Trip.objects.get(uuid=uuid)

    context = {
        "trip":trip
    }

    return render(request, 'trips/detail.html', context)

def trip_edit(request, uuid):
    trip = models.Trip.objects.get(uuid=uuid)

    if request.method =='POST':
        image = request.FILES.get('image')
        title_en = request.POST.get('title_en')
        title_ru = request.POST.get('title_ru')
        title_fr = request.POST.get('title_fr')
        title_de = request.POST.get('title_de')
        title_es = request.POST.get('title_es')
        subtitle_en = request.POST.get('subtitle_en')
        subtitle_ru = request.POST.get('subtitle_ru')
        subtitle_fr = request.POST.get('subtitle_fr')
        subtitle_de = request.POST.get('subtitle_de')
        subtitle_es = request.POST.get('subtitle_es')

        if image:
            trip.image = image
        trip.title_en = title_en
        trip.title_ru = title_ru
        trip.title_fr = title_fr
        trip.title_de = title_de
        trip.title_es = title_es
        trip.subtitle_en = subtitle_en
        trip.subtitle_ru = subtitle_ru
        trip.subtitle_fr = subtitle_fr
        trip.subtitle_de = subtitle_de
        trip.subtitle_es = subtitle_es

        trip.save()
        messages.success(request, "Trip edited successfully")
        return redirect('trip_detail', trip.uuid)

def trip_delete(request, uuid):
    trip = models.Trip.objects.get(uuid=uuid)
    if request.method == 'POST':
        trip.is_active = False
        trip.save()
        messages.success(request, "Trip deleted successfully")
        return redirect('trip_list')

def trip_create(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        title_en = request.POST.get('title_en')
        subtitle_en = request.POST.get('subtitle_en')

        new_trip = models.Trip.objects.filter.create(
            image = image, 
            title_en = title_en,
            subtitle_en = subtitle_en
        )
        messages.success(request, 'Trip created successfully')
        return redirect('trip_detail', new_trip.uuid)
