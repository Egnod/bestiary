from graphene import ObjectType, Schema

from bestiary.apps.user.api.queries import UserQuery
from bestiary.apps.user.api.mutations import RegistrationUser

from bestiary.apps.subject.api.queries import SubjectQuery


class Query(UserQuery, SubjectQuery, ObjectType):
    pass


class Mutation(ObjectType):
    registerUser = RegistrationUser.Field()


schema = Schema(query=Query, mutation=Mutation)
