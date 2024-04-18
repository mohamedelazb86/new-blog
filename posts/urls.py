from django.urls import path
from .views import post_detail,post_list,create_post

urlpatterns = [
    path('',post_list),
    path('create_post',create_post),
    path('<slug:slug>',post_detail),
    
]
