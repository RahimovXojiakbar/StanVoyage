from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.list, name='list_page'),
    path('dashboard/', include('dashboard.urls')),
    path('api/', include('api.urls')),

]


