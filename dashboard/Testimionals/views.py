from django.shortcuts import render, redirect
from main import models
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def testimionals_list(request):
    testimionals = models.Testimionals.objects.filter(is_active=True)

    context = {
        "testimionals":testimionals
    }

    return render(request, 'testimionals/list.html', context)

@login_required(login_url='login')
def testimionals_detail(request, uuid):
    testimional = models.Testimionals.objects.get(uuid=uuid)

    context = {
        "testimional":testimional
    }
    return render(request, "testimionals/detail.html" , context)

@login_required(login_url='login')
def testimionals_create(request):
    if request.method == 'POST':
        author = request.POST.get('author')
        content_en = request.POST.get('content_en')

        new_testimional = models.Testimionals.objects.create(
            author = author,
            content_en = content_en
        )
        messages.success(request, "Fikr muvaffaqiyatli yaratildi")
        return redirect('testimionals_detail', new_testimional.uuid)
    
@login_required(login_url='login')
def testimionals_update(request, uuid):
    testimional = models.Testimionals.objects.get(uuid=uuid)

    if request.method == 'POST':
        testimional.author = request.POST.get('author')
        testimional.content_en = request.POST.get('content_en')
        testimional.content_ru = request.POST.get('content_ru')
        testimional.content_fr = request.POST.get('content_fr')
        testimional.content_de = request.POST.get('content_de')
        testimional.content_es = request.POST.get('content_es')

        testimional.save()
        messages.success(request, 'Fikr muvaffaqiyatli yangilandi')
        return redirect('testimionals_detail', testimional.uuid)
    
@login_required(login_url='login')   
def testimionals_delete(request, uuid):
    testimional = models.Testimionals.objects.get(uuid=uuid)

    if request.method == 'POST':
        testimional.is_active = False
        testimional.save()
        messages.success(request, 'Fikr muvaffaqiyatli o\'chirildi')
        return redirect(request.META.get('HTTP_REFERER'))
    