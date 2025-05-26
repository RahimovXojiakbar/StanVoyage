from django.shortcuts import render, redirect
from main import models
from django.contrib import messages


def our_mission_list(request):
    our_missions = models.OurMission.objects.filter(is_active=True)
    context = {
        'our_missions': our_missions
    }
    return render(request, 'our_missions/list.html', context)




def our_mission_detail(request, uuid):
    our_mission = models.OurMission.objects.get(uuid=uuid)
    context = {
        'our_mission': our_mission
    }
    return render(request, 'our_missions/detail.html', context)

def our_mission_create(request):
    if request.method == 'POST':
        title_en = request.POST.get('title_en')
        content_en = request.POST.get('content_en')
        image = request.FILES.get('image')

        new_our_mission = models.OurMission.objects.create(
            title_en=title_en,
            content_en=content_en,
            image=image,
        )
        messages.success(request, 'Bizning vazifa muvaffaqiyatli yaratildi!')
        return redirect('ourmission_detail', new_our_mission.uuid)



def our_mission_delete(request, uuid):
    our_mission = models.OurMission.objects.get(uuid=uuid)
    if request.method == 'POST':
        our_mission.is_active = False
        our_mission.save()
        
    messages.success(request, 'Bizning vazifa muvaffaqiyatli o\'chirildi!')
    return redirect('ourmission_list')



def our_mission_edit(request, uuid):
    our_mission = models.OurMission.objects.get(uuid=uuid)
    if request.method == 'POST':
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

        image = request.FILES.get('image')

        if image:
            our_mission.image = image
        our_mission.title_en = title_en
        our_mission.title_ru = title_ru
        our_mission.title_fr = title_fr
        our_mission.title_de = title_de
        our_mission.title_es = title_es
        our_mission.content_en = description_en
        our_mission.content_ru = description_ru
        our_mission.content_fr = description_fr
        our_mission.content_de = description_de
        our_mission.content_es = description_es
            
        our_mission.save()
        messages.success(request, 'Bizning vazifa muvaffaqiyatli tahrirlandi!')
        return redirect('ourmission_detail', our_mission.uuid)




