from rest_framework import serializers

from krankit.blog.models import Post, PostComment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "slug", "author", "content", "published_on"]

        extra_kwargs = {"url": {"view_name": "api:post-detail", "lookup_field": "slug"}}


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = ["content", "owner", "post", "created_on", "active"]

        extra_kwargs = {
            "url": {"view_name": "api:comment-detail", "lookup_field": "post__id"}
        }
