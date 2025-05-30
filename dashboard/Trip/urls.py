from django.urls import path
from . import views

urlpatterns = [
    path('trips/list/', views.trip_list, name='trip_list'),
    path('trip/detail/<str:uuid>/', views.trip_detail, name='trip_detail'),
    path('trip/edit/<str:uuid>/', views.trip_edit, name='trip_edit'),
    path('trip/delete/<str:uuid>/', views.trip_delete, name='trip_delete'),
    path('trip/create/', views.trip_create, name='trip_create'),
    path('trips/reorder/', views.trip_reorder, name='trip_reorder'),

    path('trip/service/detail/<str:uuid>/', views.service_detail, name='service_detail'),
    path('trip/service/create/<str:uuid>/', views.service_create, name='service_create'),
    path('trip/service/update/<str:uuid>/', views.service_update, name='service_update'),
    path('trip/service/delete/<str:uuid>/', views.service_delete, name='service_delete'),

    path('trip/trip/days/detail/<str:uuid>/', views.trip_days_detail, name='trip_days_detail'),
    path('trip/trip/days/create/<str:uuid>/', views.trip_days_create, name='trip_days_create'),
    path('trip/trip/days/update/<str:uuid>/', views.trip_days_update, name='trip_days_update'),
    path('trip/trip/days/delete/<str:uuid>/', views.trip_days_delete, name='trip_days_delete'),

    path('trip/trip/images/create/<str:uuid>/', views.trip_images_create, name='trip_images_create'),
    path('trip/trip/images/update/<str:uuid>/', views.trip_images_update, name='trip_images_update'),
    path('trip/trip/images/delete/<str:uuid>/', views.trip_images_delete, name='trip_images_delete'),

    path('trip/orders/', views.trip_order_list, name='trip_order_list'),
    path('trip/orders/read/<str:uuid>/', views.mark_as_read, name='mark_as_read'),
]