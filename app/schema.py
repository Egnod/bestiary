from graphene import ObjectType, Schema

from apps.user.api.queries import UserQuery


class Query(UserQuery, ObjectType):
    pass


schema = Schema(query=Query)
