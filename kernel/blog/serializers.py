from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'content', 'publishe_at', 'banner', 'category', 'tag', 'author' )
