from django.urls import path
from . import views

urlpatterns = [
    path('social/', views.social, name='social'),
    path('social/edit/<str:uuid>/', views.social_edit, name='social_edit'),
    path('social/create/', views.social_create, name='social_create'),

    
    path('company-info/', views.company_info, name='company_info'),
    path('company-info/edit/<str:uuid>/', views.company_info_edit, name='company_info_edit'),
    path('company-info/create/', views.company_info_create, name='company_info_create'),

    path('contact/list/', views.contact_list, name='contact_list'),
    path('contact/read/<uuid:pk>/', views.mark_as_read, name='mark_as_read'),


]