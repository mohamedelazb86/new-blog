from rest_framework import generics
from .serializers import PostDetaiSerializers,PostListSerializers,PostUPdateCreateDelete,PostUPdateCreateDelete
from .models import Post

class PostListApi(generics.ListAPIView):
    queryset=Post.objects.all()
    serializer_class=PostListSerializers

class PostDetailApi(generics.RetrieveAPIView):
    queryset=Post.objects.all()
    serializer_class=PostDetaiSerializers
class PostAll(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostUPdateCreateDelete