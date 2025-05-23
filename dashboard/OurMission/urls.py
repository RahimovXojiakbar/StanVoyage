from django.urls import path
from . import views

urlpatterns = [
    path('ourmission/list/', views.our_mission_list, name='ourmission_list'),
    path('ourmission/detail/<str:uuid>/', views.our_mission_detail, name='ourmission_detail'),
    path('ourmission/edit/<str:uuid>/', views.our_mission_edit, name='ourmission_edit'),
    path('ourmission/delete/<str:uuid>/', views.our_mission_delete, name='ourmission_delete'),
    path('ourmission/create/', views.our_mission_create, name='ourmission_create'),
]