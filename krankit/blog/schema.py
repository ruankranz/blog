import graphene

from graphene_django.types import DjangoObjectType
from krankit.blog.models import Post, PostComment


class PostType(DjangoObjectType):
    class Meta:
        model = Post


class PostCommentType(DjangoObjectType):
    class Meta:
        model = PostComment


class Query:
    posts = graphene.List(PostType)
    post = graphene.Field(PostType, post_id=graphene.String())

    comments = graphene.List(PostCommentType)
    comment = graphene.Field(PostCommentType, comment_id=graphene.String())

    def resolve_posts(self, info, **kwargs):
        return Post.objects.all()

    def resolve_post(self, info, post_id):
        return Post.objects.get(pk=post_id)

    def resolve_comments(self, info, **kwargs):
        return PostComment.objects.all()

    def resolve_comment(self, info, comment_id):
        return PostComment.objects.get(pk=comment_id)
