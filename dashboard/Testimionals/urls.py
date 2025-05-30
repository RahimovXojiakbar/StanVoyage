from django.urls import path
from . import views

urlpatterns = [
    path('testimionals/list/', views.testimionals_list, name='testimionals_list'),
    path('testimionals/detail/<str:uuid>/', views.testimionals_detail, name='testimionals_detail'),
    path('testimionals/create/', views.testimionals_create, name='testimionals_create'),
    path('testimionals/update/<str:uuid>/', views.testimionals_update, name='testimionals_update'),
    path('testimionals/delete/<str:uuid>/', views.testimionals_delete, name='testimionals_delete'),
]