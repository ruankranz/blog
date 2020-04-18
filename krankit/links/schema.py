import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from django_filters import FilterSet

from krankit.links.models import Link, LinkVote


class LinkFilter(FilterSet):
    class Meta:
        model = Link
        fields = ["url", "description", "posted_by"]


class VoteFilter(FilterSet):
    class Meta:
        model = LinkVote
        fields = ["link_id", "link__posted_by"]


class LinkNode(DjangoObjectType):
    class Meta:
        model = Link
        interfaces = (graphene.relay.Node,)


class VoteNode(DjangoObjectType):
    class Meta:
        model = LinkVote
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    link = graphene.relay.Node.Field(LinkNode)
    all_links = DjangoFilterConnectionField(LinkNode, filterset_class=LinkFilter)

    vote = graphene.relay.Node.Field(VoteNode)
    all_votes = DjangoFilterConnectionField(VoteNode, filterset_class=VoteFilter)


class CreateLink(graphene.relay.ClientIDMutation):
    link = graphene.Field(LinkNode)

    class Input:
        url = graphene.String()
        description = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        user = info.context.user or None

        link = Link(
            url=input.get("url"), description=input.get("description"), posted_by=user
        )
        link.save()

        return CreateLink(link=link)


class Mutation(graphene.AbstractType):
    create_link = CreateLink.Field()
