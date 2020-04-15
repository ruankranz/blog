from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from krankit_news.core.models import Post, Comment


class PostNode(DjangoObjectType):
    class Meta:
        model = Post
        filter_fields = ['title', 'slug', 'author', 'created_on', 'updated_on']
        interfaces = (relay.Node, )



class CommentNode(DjangoObjectType):
    class Meta:
        model = Comment
        filter_fields = {
            'content': ['exact', 'icontains', 'istartswith'],
            'owner': ['exact'],
            'post': ['exact'],
            'post__slug': ['exact'],
        }
        interfaces = (relay.Node, )


class Query(ObjectType):
    post = relay.Node.Field(PostNode)
    all_posts = DjangoFilterConnectionField(PostNode)

    comment = relay.Node.Field(CommentNode)
    all_comments = DjangoFilterConnectionField(CommentNode)