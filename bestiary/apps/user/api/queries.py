import graphene

from bestiary.apps.user.api.types import *
from flask_jwt import jwt_required, current_identity


class UserQuery(object):
    users = graphene.List(lambda: User)
    user_by_id = graphene.Field(lambda: User, user_id=graphene.Int())
    profile = graphene.Field(lambda: User)

    def resolve_users(self, info):
        return UserModel.query.all()

    def resolve_user_by_id(self, info, user_id):
        return UserModel.query.get(user_id)

    @jwt_required()
    def resolve_profile(self, info):
        return UserModel.query.get(current_identity.id)
