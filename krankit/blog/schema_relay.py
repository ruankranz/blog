import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from krankit.blog.models import Post, PostComment


class PostNode(DjangoObjectType):
    class Meta:
        model = Post
        interfaces = (relay.Node,)
        filter_fields = {
            "title": ["exact", "icontains", "istartswith"],
            "slug": ["exact"],
            "status": ["exact"],
            "author_id": ["exact"],
            "published_on": ["exact"],
        }


class CommentNode(DjangoObjectType):
    class Meta:
        model = PostComment
        interfaces = (relay.Node,)
        filter_fields = {
            "content": ["icontains", "istartswith"],
            "user": ["exact"],
            "post_id": ["exact"],
            "post__slug": ["exact"],
            "post__title": ["exact"],
            "post__author_id": ["exact"],
        }


class Query(ObjectType):
    post = relay.Node.Field(PostNode)
    all_posts = DjangoFilterConnectionField(PostNode)

    comment = relay.Node.Field(CommentNode)
    all_comments = DjangoFilterConnectionField(CommentNode)


class CreatePost(graphene.relay.ClientIDMutation):
    post = graphene.Field(PostNode)

    class Input:
        title = graphene.String()
        content = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        user = info.context.user or None

        post = Post(title=input.get("title"), content=input.get("content"), author=user)
        post.save()

        return CreatePost(post=post)


class CreateComment(graphene.relay.ClientIDMutation):
    comment = graphene.Field(PostNode)

    class Input:
        content = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        user = info.context.user or None

        comment = PostComment(content=input.get("content"), user=user)
        comment.save()

        return CreateComment(comment=comment)


class Mutation(graphene.AbstractType):
    create_post = CreatePost.Field()
    create_comment = CreateComment.Field()
