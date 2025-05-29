from django.shortcuts import render, redirect
from main import models
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def about(request):
    about = models.AboutUs.objects.filter(is_active=True)

    context = {
        'about': about
    }
    return render(request, 'about/about.html', context)


@login_required(login_url='login')
def about_create(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        title_en = request.POST.get('title_en')
        description_en = request.POST.get('description_en')

        models.AboutUs.objects.create(
            image=image,
            title_en=title_en,
            description_en=description_en
        )
        messages.success(request, 'About muvaffaqiyatli yaratildi!')
        return redirect('about')
        
@login_required(login_url='login')
def about_edit(request, uuid):
    about = models.AboutUs.objects.get(uuid=uuid)

    if request.method == 'POST':
        # Update only provided fields
        if request.FILES.get('image'):
            about.image = request.FILES.get('image')
        about.title_en = request.POST.get('title_en')
        about.title_ru = request.POST.get('title_ru')
        about.title_fr = request.POST.get('title_fr')
        about.title_de = request.POST.get('title_de')
        about.title_es = request.POST.get('title_es')
        about.description_en = request.POST.get('description_en')
        about.description_ru = request.POST.get('description_ru')
        about.description_fr = request.POST.get('description_fr')
        about.description_de = request.POST.get('description_de')
        about.description_es = request.POST.get('description_es')
        
        about.save()
        messages.success(request, 'About muvaffaqiyatli yangilandi!')
        return redirect('about')




@login_required(login_url='login')
def why_us(request):
    why_us = models.WhyUs.objects.filter(is_active=True)

    context = {
        'why_us': why_us
    }
    return render(request, 'about/why_us.html', context)


@login_required(login_url='login')
def why_us_create(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        title_en = request.POST.get('title_en')
        content_en = request.POST.get('content_en')

        models.WhyUs.objects.create(
            image=image,
            title_en=title_en,
            content_en=content_en
        )
        messages.success(request, 'Ozimiz haqida muvaffaqiyatli yaratildi!')
        return redirect('whyus')
    
@login_required(login_url='login')
def why_us_edit(request, uuid):
    why_us = models.WhyUs.objects.get(uuid=uuid)

    if request.method == 'POST':
        # Update only provided fields
        if request.FILES.get('image'):
            why_us.image = request.FILES.get('image')
        why_us.title_en = request.POST.get('title_en')
        why_us.title_ru = request.POST.get('title_ru')
        why_us.title_fr = request.POST.get('title_fr')
        why_us.title_de = request.POST.get('title_de')
        why_us.title_es = request.POST.get('title_es')
        why_us.content_en = request.POST.get('content_en')
        why_us.content_fr = request.POST.get('content_fr')
        why_us.content_ru = request.POST.get('content_ru')
        why_us.content_de = request.POST.get('content_de')
        why_us.content_es = request.POST.get('content_es')
        
        why_us.save()
        messages.success(request, 'Ozimiz haqida muvaffaqiyatli yangilandi!')
        return redirect('whyus')