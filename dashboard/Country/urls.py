from django.urls import path
from . import views

urlpatterns = [
    path('countries/list/', views.country_list, name='country_list'),
    path('country/detail/<str:uuid>/', views.country_detail, name='country_detail'),
    path('country/edit/<str:uuid>/', views.country_edit, name='country_edit'),
    path('country/delete/<str:uuid>/', views.country_delete, name='country_delete'),
    path('country/create/', views.country_create, name='country_create'),    

    path('country/locations/<str:uuid>/', views.locations_detail, name='location_detail'),
    path('country/location/edit/<str:uuid>/', views.location_edit, name='location_edit'),
    path('country/location/delete/<str:uuid>/', views.location_delete, name='location_delete'),
    path('location/create/<uuid:uuid>/', views.location_create, name='location_create'),
]
