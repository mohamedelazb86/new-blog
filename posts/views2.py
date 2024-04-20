from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post

class Post_List(ListView):
    model=Post
    
    template_name='posts/post_list.html'

class Post_Detail(DetailView):
    model=Post
    template_name='posts/post_detail.html'


class Post_Update(UpdateView):
    model=Post
    fields='__all__'
    template_name='posts/update_post.html'

class Create_Post(CreateView):
    model=Post
    fields='__all__'
    template_name='posts/create_post.html'


