from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from krankit.blog.models import Post, PostComment


class PostNode(DjangoObjectType):
    class Meta:
        model = Post
        filter_fields = ["title", "slug", "author", "created_on", "updated_on"]
        interfaces = (relay.Node,)


class PostCommentNode(DjangoObjectType):
    class Meta:
        model = PostComment
        filter_fields = {
            "content": ["exact", "icontains", "istartswith"],
            "owner": ["exact"],
            "post": ["exact"],
            "post__slug": ["exact"],
        }
        interfaces = (relay.Node,)


class Query(ObjectType):
    post = relay.Node.Field(PostNode)
    all_posts = DjangoFilterConnectionField(PostNode)

    comment = relay.Node.Field(PostCommentNode)
    all_comments = DjangoFilterConnectionField(PostCommentNode)
