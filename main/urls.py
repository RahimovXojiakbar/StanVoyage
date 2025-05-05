from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.list, name='list_page'),
    path('detail_page/', views.detail, name='detail_page'),
    path('dashboard/', include('dashboard.urls')),
    path('api/', include('api.urls')),

]


