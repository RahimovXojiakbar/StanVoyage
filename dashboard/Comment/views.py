from django.shortcuts import render, redirect
from main import models
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt
def comment_reorder(request):
    if request.method == "POST":
        order = json.loads(request.POST.get("order", "[]"))
        for index, uuid in enumerate(order):
            models.Comment.objects.filter(uuid=uuid).update(order=index)
        return JsonResponse({"status": "ok"})
    return JsonResponse({"status": "fail"}, status=400)

def comment_list(request):
    comments = models.Comment.objects.filter(is_active=True).order_by('order')

    context = {
        "comments":comments
    }
    return render(request, "comment/list.html", context)

def comment_detail(request, uuid):
    comment = models.Comment.objects.get(uuid=uuid)

    context = {
        "comment":comment
    }
    return render(request, 'comment\detail.html', context)

def comment_create(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        fullname = request.POST.get('fullname')
        text = request.POST.get('text')

        new_comment = models.Comment.objects.create(
            image = image,
            fullname = fullname,
            text = text
        )
        messages.success(request, 'Izox muvaffaqiyatli yaratildi!')
        return redirect('comment_detail', new_comment.uuid)

def comment_update(request, uuid):
    comment = models.Comment.objects.get(uuid=uuid)

    if request.method == 'POST':
        image = request.FILES.get('image')
        fullname = request.POST.get('fullname')
        text = request.POST.get('text')

        if image:
            comment.image = image
        comment.fullname = fullname
        comment.text = text

        comment.save()
        messages.success(request, "Izox muvaffaqiyatli yangilandi")
        return redirect('comment_detail', comment.uuid)
    return render(request, 'comment/detail.html', {'comment': comment})

def comment_delete(request, uuid):
    comment = models.Comment.objects.get(uuid=uuid)

    if request.method == 'POST':
        comment.is_active = False
        comment.save()
        messages.success(request, "Izox muvaffaqiyatli o\'chirildi!")
        return redirect('comment_list')
    
