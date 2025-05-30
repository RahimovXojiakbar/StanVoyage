from django.shortcuts import render, redirect
from main.models import Gallery
from django.contrib import messages
from django.contrib.auth.decorators import login_required



@login_required(login_url='login')
def gallery_list(request):
    galery = Gallery.objects.filter(is_active=True)

    context = {
        'galery': galery
    }
    return render(request, 'gallery/list.html', context)

@login_required(login_url='login')
def gallery_create(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        title_en = request.POST.get('title_en')
    
        new_gallery = Gallery.objects.create(
            image = image,
            title_en = title_en,
        )
        messages.success(request, 'Galereya muvaffaqiyatli yaratildi!')
        return redirect('gallery_list')

@login_required(login_url='login')
def gallery_delete(request, uuid):
    gallery = Gallery.objects.get(uuid=uuid)
    if request.method == 'POST':
        gallery.is_active = False
        gallery.save()
        messages.success(request, 'Galereya muvaffaqiyatli o\'chirildi!')
        return redirect('gallery_list')

@login_required(login_url='login')
def gallery_edit(request, uuid):
    if request.method == 'POST':
        image = request.FILES.get('image')
        title_en = request.POST.get('title_en')
        title_ru = request.POST.get('title_ru')
        title_fr = request.POST.get('title_fr')
        title_de = request.POST.get('title_de')
        title_es = request.POST.get('title_es')

        gallery = Gallery.objects.get(uuid=uuid)
        if image:
            gallery.image = image
        gallery.title_en = title_en
        gallery.title_ru = title_ru
        gallery.title_fr = title_fr
        gallery.title_de = title_de
        gallery.title_es = title_es
        gallery.save()
        messages.success(request, 'Galereya muvaffaqiyatl yangilandi!')
        return redirect('gallery_list')
