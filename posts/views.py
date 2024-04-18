from django.shortcuts import render,redirect
from .models import Post,Comment
from .form import PostForm,CommentForm
# create crud operation by fbv

def post_list(request):
    data= Post.objects.all()

    context={
        'posts':data
    }

    return render(request,'posts/post_list.html',context)

def post_detail(request,slug):
    post=Post.objects.get(slug=slug)
    comments=Comment.objects.filter(post=post)
    if request.method=='POST':
        form=CommentForm(request.POST)
        form.is_valid()
        myform=form.save(commit=False)
        myform.post=post
        form.save()
        return redirect('/posts/')
    else:
        form=CommentForm()


    context={
        'post':post,
        'comments':comments,
        'form':form,
    }

    return render(request,'posts/post_detail.html',context)

def create_post(request):
    if request.method =='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.user=request.user
            form.save()
            return redirect('/posts/')
    else:
        form=PostForm()
    return render(request,'posts/create_post.html',{'form':form})

def delete_post(request,id):
    post=Post.objects.get(id=id)
    post.delete()
    return redirect('/posts/')

def Update_post(request,id):
    post=Post.objects.get(id=id)
    if request.method == 'POST':
        form=PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            myform=form.save(commit=False)
            form.save()
            return redirect('/posts/')
    else:
        form=PostForm(instance=post)
    return render(request,'posts/update_post.html',{'form':form})

