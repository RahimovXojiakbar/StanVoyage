from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from main import models
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def tradition_list(request):
    traditions = models.Traditions.objects.filter(is_active=True)
    context = {
        'traditions': traditions
    }
    return render(request, 'traditions/list.html', context)

@login_required(login_url='login')
def tradition_detail(request, uuid):
    tradition = get_object_or_404(models.Traditions, uuid=uuid)
    context = {
        'tradition': tradition
    }
    return render(request, 'traditions/detail.html', context)

@login_required(login_url='login')
def tradition_edit(request, uuid):
    tradition = get_object_or_404(models.Traditions, uuid=uuid)
    if request.method == 'POST':
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
            tradition.image = image
        tradition.title_en = title_en
        tradition.title_ru = title_ru
        tradition.title_fr = title_fr
        tradition.title_de = title_de
        tradition.title_es = title_es

        tradition.subtitle_en = subtitle_en
        tradition.subtitle_ru = subtitle_ru
        tradition.subtitle_fr = subtitle_fr
        tradition.subtitle_de = subtitle_de
        tradition.subtitle_es = subtitle_es

        tradition.save()
        messages.success(request, 'Tradition successfully updated!')
        return redirect('tradition_detail', tradition.uuid)
    
    context = {'tradition': tradition}
    return render(request, 'traditions/edit.html', context)

@login_required(login_url='login')
def tradition_create(request):
    if request.method == 'POST':
        subtitle_en = request.POST.get('subtitle_en')
        title_en = request.POST.get('title_en')
        content_en = request.POST.get('content_en')

        new_tradition = models.Traditions.objects.create(
            subtitle_en=subtitle_en,
            title_en=title_en,
            content_en=content_en
        )
        messages.success(request, 'Tradition successfully created!')
        return redirect('tradition_detail', new_tradition.uuid)


@login_required(login_url='login')
def tradition_delete(request, uuid):
    tradition = get_object_or_404(models.Traditions, uuid=uuid)
    if request.method == 'POST':
        tradition.is_active = False
        tradition.save()
        messages.success(request, 'Tradition successfully deleted')
    return redirect('tradition_list')