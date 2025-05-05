from django.shortcuts import render

def list(request):
    return render(request, 'list_page.html')


def detail(request):
    return render(request, 'detail_page.html')


