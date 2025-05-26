from django.urls import path
from . import views


urlpatterns = [
    path('social/', views.social, name='social'),
    path('contact/', views.contact, name='contact'),
    path('company-info/', views.companyInfo, name='company-info'),
    path('banner/', views.banner, name='banner'),
    path('banner-detail/<str:uuid>/', views.bannerDetail, name='banner-detail'),
    path('why-us/', views.whyUs, name='why-us'),
    path('our-mission/', views.ourMission, name='our-mission'),
    path('instruction/', views.instructions, name='instruction'),
    path('blog/', views.blog, name='blog'),
    path('blog-detail/<str:uuid>/', views.blogDetail, name='blog-detail'),
    path('comment/', views.comment, name='comment'),
    path('traditions/', views.traditions, name='traditions'),
    path('testimionals/', views.testimionals, name='testimionals'),
    path('country/', views.country, name='country'),
    path('country-detail/<str:uuid>/', views.countryDetail, name='country-detail'),
    path('location-detail/<str:uuid>/', views.locationDetail, name='location-detail'),
    path('trip/', views.trip, name='trip'),
    path('trip-detail/<str:uuid>/', views.tripDetail, name='trip-detail'),
]