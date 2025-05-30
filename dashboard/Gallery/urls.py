from django.urls import path
from . import views

urlpatterns = [
    path('gallery/list/', views.gallery_list, name='gallery_list'),
    path('gallery/delete/<str:uuid>/', views.gallery_delete, name='gallery_delete'),
    path('gallery/create/', views.gallery_create, name='gallery_create'),
    path('gallery/edit/<str:uuid>/', views.gallery_edit, name='gallery_edit'),

]