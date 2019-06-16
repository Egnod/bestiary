import graphene

from apps.user.api.types import *


class UserQuery(object):
    users = graphene.List(lambda: User)

    def resolve_users(self, info):
        return UserModel.query.all()
