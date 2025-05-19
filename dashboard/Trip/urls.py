from django.urls import path
from . import views

urlpatterns = [
    path('trips/list/', views.trip_list, name='trip_list'),
    path('trip/detail/<str:uuid>/', views.trip_detail, name='trip_detail'),
    path('trip/edit/<str:uuid>/', views.trip_edit, name='trip_edit'),
    path('trip/delete/<str:uuid>/', views.trip_delete, name='trip_delete'),
    path('trip/create/', views.trip_create, name='trip_create'),
    path('trips/reorder/', views.trip_reorder, name='trip_reorder'),

]