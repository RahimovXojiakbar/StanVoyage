from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def list(request):
    return render(request, 'list_page.html')


@login_required(login_url='login')
def detail(request):
    return render(request, 'detail_page.html')


