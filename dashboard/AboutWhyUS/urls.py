from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('about/create/', views.about_create, name='about_create'),
    path('about/edit/<str:uuid>/', views.about_edit, name='about_edit'),


    path('whyus/', views.why_us, name='whyus'),
    path('whyus/create/', views.why_us_create, name='whyus_create'),
    path('whyus/edit/<str:uuid>/', views.why_us_edit, name='whyus_edit'),   
]

