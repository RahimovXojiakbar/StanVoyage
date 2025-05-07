from django.shortcuts import render
from main import models

def blog_list(request):
    blog = models.Blog.objects.filter(is_active = True)
    context = {
        'blogs':blog
    }
    return render(request, 'blog/list.html', context)   