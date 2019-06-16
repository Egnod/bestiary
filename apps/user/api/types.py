from graphene_sqlalchemy import SQLAlchemyObjectType

from apps.user.models import User as UserModel
from apps.user.models import UserDetail as UserDetailModel


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        exclude_fields = ("_password_hash", "_login")


class UserDetail(SQLAlchemyObjectType):
    class Meta:
        model = UserDetailModel
