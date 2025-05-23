from django.shortcuts import render, redirect
from main.models import Gallery
from django.contrib import messages




def gallery_list(request):
    galery = Gallery.objects.filter(is_active=True)

    context = {
        'galery': galery
    }
    return render(request, 'gallery/list.html', context)


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


def gallery_delete(request, uuid):
    gallery = Gallery.objects.get(uuid=uuid)
    if request.method == 'POST':
        gallery.is_active = False
        gallery.save()
        messages.success(request, 'Galereya muvaffaqiyatli o\'chirildi!')
        return redirect('gallery_list')


def gallery_edit(request, uuid):
    if request.method == 'POST':
        image = request.FILES.get('image')
        title_en = request.POST.get('title_en')
        gallery = Gallery.objects.get(uuid=uuid)
        if image:
            gallery.image = image
        gallery.title_en = title_en
        gallery.save()
        messages.success(request, 'Galereya muvaffaqiyatl yangilandi!')
        return redirect('gallery_list')
