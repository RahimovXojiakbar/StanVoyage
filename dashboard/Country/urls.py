from django.urls import path
from . import views

urlpatterns = [
    #Country / Trip start

    path('countries/list/', views.country_list, name='country_list'),
    path('country/detail/<str:uuid>/', views.country_detail, name='country_detail'),

    #Country / Trip end
]
