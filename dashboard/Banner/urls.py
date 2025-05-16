from django.urls import path
from . import views 


urlpatterns = [ 
    
    path('banner/list/',  views.banner_list, name='banner_list'),
    path('banner/detail/<str:uuid>/', views.banner_detail, name='banner_detail'),
    path('banner/edit/<str:uuid>/', views.banner_edit, name='banner_edit'),
    path('banner/delete/<str:uuid>/', views.banner_delete, name='banner_delete'),
    path('banner/create/', views.banner_create, name='banner_create'),
    ] 














































