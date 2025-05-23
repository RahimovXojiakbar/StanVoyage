from django.urls import path
from . import views 


urlpatterns = [ 
    
    path('banner/list/',  views.banner_list, name='banner_list'),
    path('banner/detail/<str:uuid>/', views.banner_detail, name='banner_detail'),
    path('banner/edit/<str:uuid>/', views.banner_edit, name='banner_edit'),
    path('banner/delete/<str:uuid>/', views.banner_delete, name='banner_delete'),
    path('banner/create/', views.banner_create, name='banner_create'),

    path('banner/SmallBanner/create/<str:uuid>/', views.SmallBanner_create, name='SmallBanner_create'), 
    path('banner/SmallBanner/edit/<str:uuid>/', views.SmallBanner_edit, name='SmallBanner_edit'), 
    path('banner/SmallBanner/delete/<str:uuid>/', views.SmallBanner_delete, name='SmallBanner_delete'),

    ] 














































