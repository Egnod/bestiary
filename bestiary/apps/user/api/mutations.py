import graphene

from bestiary.apps.user.api.types import *
from bestiary.app import db


class RegistrationUserDetail(graphene.InputObjectType):
    first_name = graphene.String(required=True)
    about = graphene.String()


class RegistrationUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

        user_detail = RegistrationUserDetail()

    user = graphene.Field(User)
    user_detail = graphene.Field(UserDetail)

    @staticmethod
    def mutate(root, info, username, password, user_detail):
        user = UserModel()
        user.username = username
        user.password_hash = password

        db.session.add(user)
        db.session.commit()

        detail = UserDetailModel()
        detail.user_id = user.id
        detail.first_name = user_detail.first_name
        detail.about = user_detail.about

        db.session.add(detail)
        db.session.commit()

        return RegistrationUser(user=user, user_detail=detail)
