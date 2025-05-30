from django.urls import path
from . import views


urlpatterns = [
    path('social/', views.social, name='social_url'),
    path('contact/', views.contact, name='contact_url'),
    path('company-info/', views.companyInfo, name='company-info_url'),
    path('banner/', views.banner, name='banner'),
    path('banner-detail/<str:uuid>/', views.bannerDetail, name='banner-detail_url'),
    path('why-us/', views.whyUs, name='why-us_url'),
    path('our-mission/', views.ourMission, name='our-mission_url'),
    path('instruction/', views.instructions, name='instruction_url'),
    path('blog/', views.blog, name='blog_url'),
    path('blog-detail/<str:uuid>/', views.blogDetail, name='blog-detail_url'),
    path('comment/', views.comment, name='comment_url'),
    path('traditions/', views.traditions, name='traditions_url'),
    path('testimionals/', views.testimionals, name='testimionals_url'),
    path('country/', views.country, name='country_url'),
    path('country-detail/<str:uuid>/', views.countryDetail, name='country-detail_url'),
    path('location-detail/<str:uuid>/', views.locationDetail, name='location-detail_url'),
    path('trip/', views.trip, name='trip_url'),
    path('trip-detail/<str:uuid>/', views.tripDetail, name='trip-detail_url'),
]