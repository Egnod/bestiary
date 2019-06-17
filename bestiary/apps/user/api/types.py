from graphene_sqlalchemy import SQLAlchemyObjectType

from bestiary.apps.user.models import User as UserModel
from bestiary.apps.user.models import UserDetail as UserDetailModel


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        exclude_fields = ("_password_hash", "_username")


class UserDetail(SQLAlchemyObjectType):
    class Meta:
        model = UserDetailModel
