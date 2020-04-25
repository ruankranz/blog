import graphene
import graphql_jwt

import krankit.blog.schema
import krankit.links.schema
import krankit.users.schema


class Query(
    krankit.blog.schema.Query,
    krankit.links.schema.Query,
    krankit.users.schema.Query,
    graphene.ObjectType,
):
    pass


class Mutation(
    krankit.links.schema.Mutation, krankit.users.schema.Mutation, graphene.ObjectType
):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
