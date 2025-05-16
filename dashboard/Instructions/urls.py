from django.urls import path
from . import views

urlpatterns = [
    path('Instructions/list/', views.instructions_list, name='instructions_list'),
    path('Instructions/detail/<str:uuid>/', views.instructions_detail, name='instructions_detail'),
    path('Instructions/edit/<str:uuid>/', views.instructions_edit, name='instructions_edit'),
    path('Instructions/delete/<str:uuid>/', views.instructions_delete, name='instructions_delete'),
    path('Instructions/create/', views.instructions_create, name='instructions_create'),
]