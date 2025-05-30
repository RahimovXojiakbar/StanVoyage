from django.shortcuts import render, redirect
from main import models
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def instructions_list(request):
    instructions = models.Instructions.objects.filter(is_active=True)
    context = {
        'instructions': instructions
    }
    return render(request, 'instructions/list.html', context)


@login_required(login_url='login')
def instructions_detail(request, uuid):
    instructions = models.Instructions.objects.get(uuid=uuid)
    context = {
        'instructions': instructions
    }
    return render(request, 'instructions/detail.html', context)

@login_required(login_url='login')
def instructions_edit(request, uuid):
    instructions = models.Instructions.objects.get(uuid=uuid)

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
            instructions.image = image
        instructions.title_en = title_en
        instructions.title_ru = title_ru
        instructions.title_fr = title_fr
        instructions.title_de = title_de
        instructions.title_es = title_es
        instructions.content_en = description_en
        instructions.content_ru = description_ru
        instructions.content_fr = description_fr
        instructions.content_de = description_de
        instructions.content_es = description_es
        
        instructions.save()
    messages.success(request, 'Korsatuvchi muvaffaqiyatli tahrirlandi!')
    return redirect('instructions_detail', instructions.uuid) 


@login_required(login_url='login')
def instructions_delete(request, uuid):
    instructions = models.Instructions.objects.get(uuid=uuid)
    if request.method == 'POST':
        instructions.is_active = False
        instructions.save()
    messages.success(request, 'Korsatuvchi muvaffaqiyatli o\'chirildi!')
    return redirect('instructions_list')


@login_required(login_url='login')
def instructions_create(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        title_en = request.POST.get('title_en')
        content_en = request.POST.get('content_en')
        
        new_instructions = models.Instructions.objects.create(
            image=image,
            title_en=title_en,
            content_en=content_en
        )
        messages.success(request, 'Korsatuvchi muvaffaqiyatli yaratildi!')
        return redirect('instructions_detail', new_instructions.uuid)