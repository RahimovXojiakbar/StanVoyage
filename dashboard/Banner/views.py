import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from main import models
from django.contrib import messages


def banner_list(request):
    banners = models.Banner.objects.filter(is_active=True).order_by('order')
    context = {
        'banners': banners
    }
    return render(request, 'banner/list.html', context)


def banner_reorder(request):
    if request.method == "POST":
        order = json.loads(request.POST.get("order", "[]"))
        for index, uuid in enumerate(order):
            models.Banner.objects.filter(uuid=uuid).update(order=index)
        return JsonResponse({"status": "ok"})
    return JsonResponse({"status": "fail"}, status=400)



def banner_detail(request, uuid):
    banner = models.Banner.objects.get(uuid=uuid)
    small_banner = models.SmallBanner.objects.filter(banner = banner, is_active=True)
    context = {
        'banner': banner,
        'small_banners':small_banner
    }
    return render(request, 'banner/detail.html', context)


def banner_edit(request, uuid):
    banner = models.Banner.objects.get(uuid=uuid)

    if request.method == 'POST':
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
            banner.image = image
        banner.title_en = title_en
        banner.title_ru = title_ru
        banner.title_fr = title_fr
        banner.title_de = title_de
        banner.title_es = title_es
        banner.description_en = description_en
        banner.description_ru = description_ru
        banner.description_fr = description_fr
        banner.description_de = description_de
        banner.description_es = description_es
        
        banner.save()
    messages.success(request, 'Banner muvaffaqiyatl yangilandi!')
    return redirect('banner_detail', uuid=banner.uuid) 



def banner_delete(request, uuid):
    banner = models.Banner.objects.get(uuid=uuid)
    if request.method == 'POST':
        banner.is_active = False
        banner.save()
    messages.success(request, 'Banner muvaffaqiyatli o\'chirildi!')
    return redirect('banner_list')



def banner_create(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        title_en = request.POST.get('title_en')
        description_en = request.POST.get('description_en')
        
        new_banner = models.Banner.objects.create(
            image=image,
            title_en=title_en,
            description_en=description_en
        )
        messages.success(request, 'Banner muvaffaqiyatli yaratildi!')
        return redirect('banner_detail', uuid=new_banner.uuid)





def SmallBanner_create(request, uuid):
    banner = models.Banner.objects.get(uuid=uuid)
    if request.method == 'POST':
        image = request.FILES.get('image')
        
        models.SmallBanner.objects.create(
            banner = banner,
            image=image,
        )
        return redirect(request.META.get('HTTP_REFERER', '/'))




def SmallBanner_edit(request, uuid):
    SmallBanner = models.SmallBanner.objects.get(uuid=uuid)
    if request.method == 'POST':
        image = request.FILES.get('image')
        
        if image:
            SmallBanner.image = image
        
        SmallBanner.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))




def SmallBanner_delete(request, uuid):
    SmallBanner = models.SmallBanner.objects.get(uuid=uuid)
    if request.method == 'POST':
        SmallBanner.is_active = False
        SmallBanner.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))