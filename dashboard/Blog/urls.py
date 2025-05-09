from django.urls import path
from . import views
urlpatterns = [

    path('Blog/list/', views.blog_list, name='blog_list'),
    path('blog/detail/<str:uuid>/', views.blog_detail, name='blog_detail'),
    path('blog/edit/<str:uuid>/', views.blog_edit, name='blog_edit'),
    path('blog/delete/<str:uuid>/', views.blog_delete, name='blog_delete'),
    path('blog/create/', views.blog_create, name='blog_create')

]