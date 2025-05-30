from django.shortcuts import render, redirect
from main import models
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@csrf_exempt
def trip_reorder(request):
    if request.method == "POST":
        order = json.loads(request.POST.get("order", "[]"))
        for index, uuid in enumerate(order):
            models.Trip.objects.filter(uuid=uuid).update(order=index)
        return JsonResponse({"status": "ok"})
    return JsonResponse({"status": "fail"}, status=400)

@login_required(login_url='login')
def trip_list(request):
    trips = models.Trip.objects.filter(is_active=True).order_by('order')

    context = {
        "trips":trips
    }

    return render(request, 'trips/list.html', context)

@login_required(login_url='login')
def trip_detail(request, uuid):
    trip = models.Trip.objects.get(uuid=uuid)
    trip_images = models.TripImages.objects.filter(trip=trip, is_active=True)
    trip_days = models.TripDays.objects.filter(trip=trip, is_active=True).order_by('order')
    services = models.Service.objects.filter(trip=trip, is_active=True)

    context = {
        "trip": trip,
        "trip_images": trip_images,
        "trip_days": trip_days,
        "services": services
    }
    return render(request, 'trips/detail.html', context)

@login_required(login_url='login')
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
        messages.success(request, "Sayohat muvaffaqiyatli yangilandi")
        return redirect('trip_detail', trip.uuid)

@login_required(login_url='login')
def trip_delete(request, uuid):
    trip = models.Trip.objects.get(uuid=uuid)
    if request.method == 'POST':
        trip.is_active = False
        trip.save()
        messages.success(request, "Sayohat muvaffaqiyatli o'chirildi")
        return redirect('trip_list')

@login_required(login_url='login')
def trip_create(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        title_en = request.POST.get('title_en')
        subtitle_en = request.POST.get('subtitle_en')

        new_trip = models.Trip.objects.create(
            image = image, 
            title_en = title_en,
            subtitle_en = subtitle_en
        )
        messages.success(request, 'Sayohat muvaffaqiyatli yaratildi')
        return redirect('trip_detail', new_trip.uuid)



@login_required(login_url='login')
def service_detail(request, uuid):
    service = models.Service.objects.get(uuid=uuid)
    trip = service.trip

    context = {
        'service':service,
        'trip':trip
    }
    return render(request, 'trips/service_detail.html', context)

@login_required(login_url='login')
def service_create(request, uuid):
    trip = models.Trip.objects.get(uuid=uuid)
    if request.method == 'POST':
        new_serivice = models.Service.objects.create(
            trip = trip,
            image = request.FILES.get('image'),
            title_en = request.POST.get('title_en'),
            content_en = request.POST.get('content_en'),
        )
        messages.success(request, 'Xizmat muvaffaqiyatli yaratildi!')
        return redirect('service_detail', new_serivice.uuid)
    
@login_required(login_url='login')
def service_update(request, uuid):
    service = models.Service.objects.get(uuid=uuid)
    

    if request.method == 'POST':
        image = request.FILES.get('image')
        if image:
            service.image = image
        service.title_en = request.POST.get('title_en')
        service.title_ru = request.POST.get('title_ru')
        service.title_fr = request.POST.get('title_fr')
        service.title_de = request.POST.get('title_de')
        service.title_es = request.POST.get('title_es')

        service.content_en = request.POST.get('content_en')
        service.content_ru = request.POST.get('content_ru')
        service.content_fr = request.POST.get('content_fr')
        service.content_de = request.POST.get('content_de')
        service.content_es = request.POST.get('content_es')

        service.save()
        messages.success(request, 'Xizmat muvaffaqiyatli yangilandi!')
        return redirect('service_detail', service.uuid)
  
@login_required(login_url='login')
def service_delete(request, uuid):
    service = models.Service.objects.get(uuid=uuid)
    if request.method == 'POST':
        service.is_active = False
        service.save()
        messages.success(request, 'Xizmat muvaffaqiyatli o\'chirildi!')
        return redirect(request.META.get('HTTP_REFERER'))
    


@csrf_exempt
def trip_days_reorder(request):
    if request.method == "POST":
        order = json.loads(request.POST.get("order", "[]"))
        for index, uuid in enumerate(order):
            models.TripDays.objects.filter(uuid=uuid).update(order=index)
        return JsonResponse({"status": "ok"})
    return JsonResponse({"status": "fail"}, status=400)

@login_required(login_url='login')
def trip_days_detail(request, uuid):
    trip_days = models.TripDays.objects.get(uuid=uuid)
    trip = trip_days.trip

    context = {
        "trip_days":trip_days,
        'trip':trip
    }
    return render(request, 'trips/trip_days.html', context)

@login_required(login_url='login')
def trip_days_create(request, uuid):
    trip = models.Trip.objects.get(uuid=uuid)
    if request.method == 'POST':
        new_trip_day = models.TripDays.objects.create(
            trip = trip,
            title_en = request.POST.get('title_en'),
            content_en = request.POST.get('content_en')
        )
        messages.success(request, 'Sayohat kuni muvaffaqiyatli yaratildi!')
        return redirect('trip_days_detail', new_trip_day.uuid)

@login_required(login_url='login')
def trip_days_update(request, uuid):
    trip_days = models.TripDays.objects.get(uuid=uuid)

    if request.method == 'POST':
        trip_days.title_en = request.POST.get('title_en')
        trip_days.title_ru = request.POST.get('title_ru')
        trip_days.title_fr = request.POST.get('title_fr')
        trip_days.title_de = request.POST.get('title_de')
        trip_days.title_es = request.POST.get('title_es')

        trip_days.content_en = request.POST.get('content_en')
        trip_days.content_ru = request.POST.get('content_ru')
        trip_days.content_fr = request.POST.get('content_fr')
        trip_days.content_de = request.POST.get('content_de')
        trip_days.content_es = request.POST.get('content_es')

        trip_days.save()
        messages.success(request, 'Sayohat kuni muvaffaqiyatli yangilandi')
        return redirect('trip_days_detail', trip_days.uuid)
    
@login_required(login_url='login')
def trip_days_delete(request, uuid):
    trip_days = models.TripDays.objects.get(uuid=uuid)
    if request.method == 'POST':
        trip_days.is_active = False
        trip_days.save()
        messages.success(request, 'Sayohat kuni muvaffaqiyatli o\'chirildi!')
        return redirect(request.META.get('HTTP_REFERER'))



@login_required(login_url='login')
def trip_images_create(request, uuid):
    trip = models.Trip.objects.get(uuid=uuid)
    if request.method == 'POST':
        new_trip_image = models.TripImages.objects.create(
            trip = trip,
            image = request.FILES.get('image'),
        )
        messages.success(request, 'Sayohat rasmi muvaffaqiyatli yaratildi!')
        return redirect(request.META.get('HTTP_REFERER'))
    
@login_required(login_url='login')
def trip_images_update(request, uuid):
    trip_images = models.TripImages.objects.get(uuid=uuid)
    image = request.FILES.get('image')

    if request.method == 'POST':
        if image:
            trip_images.image = image

            trip_images.save()
            messages.success(request, 'Sayohat rasmi muvaffaqiyatli yangilandi!')
            return redirect(request.META.get('HTTP_REFERER'))
        
@login_required(login_url='login')
def trip_images_delete(request, uuid):
    trip_images = models.TripImages.objects.get(uuid=uuid)
    if request.method == 'POST':
        trip_images.is_active = False
        trip_images.save()
        messages.success(request, 'Sayohat rasmi muvaffaqiyatli o\'chirildi!')
        return redirect(request.META.get('HTTP_REFERER'))
    


@login_required(login_url='login')
def trip_order_list(request):
    trip_orders = models.TripOrder.objects.filter(is_active=True)

    context = {
        "trip_orders":trip_orders
    }
    return render(request, 'trips/trip_orders.html', context)

@login_required(login_url='login')
def mark_as_read(request, uuid):
    if request.method == 'POST':
        try:
            trip_order = models.TripOrder.objects.get(uuid=uuid)
            is_read = request.POST.get('is_read') == 'on'
            trip_order.is_read = is_read
            trip_order.save()
        except models.TripOrder.DoesNotExist:
            pass  # Optionally handle missing contact
    return redirect(request.META.get('HTTP_REFERER', 'list_page')) 


