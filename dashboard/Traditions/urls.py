from django.urls import path
from . import views

urlpatterns = [
    path('Traditions/list/', views.tradition_list,name='tradition_list'),
    path('Traditions/detail/<str:uuid>', views.tradition_detail,name='tradition_detail'),
    path('Traditions/create/', views.tradition_create,name='traditions_create'),
    path('Traditions/edit/<str:uuid>/', views.tradition_edit,name='tradition_edit'),
    path('Traditions/delete/<str:uuid>/', views.tradition_delete,name='tradition_delete')
]