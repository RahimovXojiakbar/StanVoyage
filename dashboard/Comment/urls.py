from django.urls import path
from . import views

urlpatterns = [
    path('comments/reorder/', views.comment_reorder, name='comment_reorder'),
    path('comment/list/', views.comment_list, name='comment_list'),
    path('comment/detail/<str:uuid>/', views.comment_detail, name='comment_detail'),
    path('comment/create/', views.comment_create, name='comment_create'),
    path('comment/update/<str:uuid>/', views.comment_update, name='comment_update'),
    path('comment/delete/<str:uuid>/', views.comment_delete, name='comment_delete'),
]