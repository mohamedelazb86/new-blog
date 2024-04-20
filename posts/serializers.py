
from .models import Post
from rest_framework import serializers

class PostListSerializers(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'
class PostDetaiSerializers(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'
class PostUPdateCreateDelete(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'