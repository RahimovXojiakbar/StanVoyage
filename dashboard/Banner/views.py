from django.shortcuts import render
from main import models


def banner_list(request):
    banners = models.Banner.objects.filter(is_active=True)
    context = {
        'banners': banners
    }
    return render(request, 'banner/list.html', context)