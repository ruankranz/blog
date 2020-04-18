import graphene

import krankit.blog.schema


class Query(krankit.blog.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
