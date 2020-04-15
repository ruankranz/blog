import graphene

import krankit_news.core.schema

class Query(krankit_news.core.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)