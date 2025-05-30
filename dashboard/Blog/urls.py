from  django.urls import path
from . import views
urlpatterns = [
    path('Blog/list/', views.blog_list, name='blog_list'),
    path('Blog/detail/<str:uuid>/', views.blog_detail, name='blog_detail'),
    path('blog/edit/<str:uuid>/', views.blog_edit, name='blog_edit'),
    path('blog/create/' , views.blog_create, name='blog_create'),
    path('blog/delete/<str:uuid>/', views.blog_delete, name='blog_delete'),

    path('blog/blog/images/create/<str:uuid>/', views.blog_images_create, name='blog_images_create'),
    path('blog/blog/images/update/<str:uuid>/', views.blog_images_update, name='blog_images_update'),
    path('blog/blog/images/delete/<str:uuid>/', views.blog_images_delete, name='blog_images_delete'),

]