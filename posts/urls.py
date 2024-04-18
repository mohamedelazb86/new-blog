from django.urls import path
from .views import post_detail,post_list,create_post,delete_post,Update_post

urlpatterns = [
    path('',post_list),
    path('create_post',create_post),
    path('<slug:slug>',post_detail),
    path('<int:id>/delete',delete_post),
    path('<int:id>/update',Update_post),
    
]
