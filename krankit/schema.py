import graphene

import krankit.blog.schema
import krankit.links.schema


class Query(krankit.blog.schema.Query, krankit.links.schema.Query, graphene.ObjectType):
    pass


class Mutation(
    krankit.links.schema.Mutation, krankit.blog.schema.Mutation, graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
