import graphene

from graphene_django.types import DjangoObjectType
from krankit.interactions.models import Comment, Vote


class VoteType(DjangoObjectType):
    class Meta:
        model = Comment


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment


class Query:
    votes = graphene.List(VoteType)
    votes = graphene.Field(VoteType, vote_id=graphene.String())

    comments = graphene.List(CommentType)
    comment = graphene.Field(CommentType, comment_id=graphene.String())

    def resolve_votes(self, info, **kwargs):
        return Vote.objects.all()

    def resolve_vote(self, info, vote_id):
        return Vote.objects.get(pk=vote_id)

    def resolve_comments(self, info, **kwargs):
        return Comment.objects.all()

    def resolve_comment(self, info, comment_id):
        return Comment.objects.get(pk=comment_id)
