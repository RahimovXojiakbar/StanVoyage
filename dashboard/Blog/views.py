from django.shortcuts import render, redirect
from main import models
from django.contrib import messages

def blog_list(request):
    blog = models.Blog.objects.filter(is_active = True)
    context = {
        'blogs':blog 
    }
    return render(request, 'blog/list.html', context)



def blog_detail(request, uuid):
    blog = models.Blog.objects.get(uuid=uuid)
    context = {
        'blog':blog
    }
    return render(request, 'blog/detail.html', context)




def blog_edit(request, uuid):
    blog = models.Blog.objects.get(uuid=uuid)
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
            blog.image = image
        blog.title_en = title_en
        blog.title_ru = title_ru
        blog.title_fr = title_fr
        blog.title_de = title_de
        blog.title_es = title_es

        blog.description_en = description_en
        blog.description_ru = description_ru
        blog.description_fr = description_fr
        blog.description_de = description_de
        blog.description_es = description_es

        blog.save()
        messages.success(request, 'Blog muvaffaqiyatli yangilandi!')
        return redirect('blog_detail', blog.uuid)


def blog_create(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        title_en = request.POST.get('title_en')
        description_en = request.POST.get('description_en')

        new_blog = models.Blog.objects.create(
            image = image,
            title_en = title_en,
            description_en = description_en
        )
        messages.success(request, 'Blog muvaffaqiyatli yaratildi!')
        return redirect('blog_detail', new_blog.uuid)


def blog_delete(request, uuid):
    blog = models.Blog.objects.get(uuid=uuid)
    if request.method == 'POST':
        blog.is_active = False
        blog.save()
        messages.success(request, 'Blog muvaffaqiyatli o\'chirildi')
    return redirect('blog_list')

