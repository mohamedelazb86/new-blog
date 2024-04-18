from django.shortcuts import render
from .models import Post
# create crud operation by fbv

def post_list(request):
    data= Post.objects.all()

    context={
        'posts':data
    }

    return render(request,'posts/post_list.html',context)

def post_detail(request,slug):
    post=Post.objects.get(slug=slug)

    context={
        'post':post
    }

    return render(request,'posts/post_detail.html',context)
