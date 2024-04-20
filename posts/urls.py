from django.urls import path
from .views import post_detail,post_list,create_post,delete_post,Update_post
from .views2 import Create_Post,Post_Update,Post_Detail,Post_List

urlpatterns = [
    path('',post_list),
    path('create_post',create_post),
    path('<slug:slug>',post_detail),
    path('<int:id>/delete',delete_post),
    path('<int:id>/update',Update_post),

    # path for crud operiation by c b v
    path('mylist/mylist/mylist',Post_List.as_view()),
    path('mylist/mylist/<int:pk>',Post_Detail.as_view()),
    path('mylist/create',Create_Post.as_view()),
    path('mylist/udate/<int:pk>',Post_Update.as_view()),
    
]
