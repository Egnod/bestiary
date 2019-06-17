from graphene_sqlalchemy import SQLAlchemyObjectType

from bestiary.apps.subject.models import Subject as SubjectModel
from bestiary.apps.subject.models import SubjectType as SubjectTypeModel
from bestiary.apps.subject.models import SubjectCategory as SubjectCategoryModel


class Subject(SQLAlchemyObjectType):
    class Meta:
        model = SubjectModel


class SubjectType(SQLAlchemyObjectType):
    class Meta:
        model = SubjectTypeModel


class SubjectCategory(SQLAlchemyObjectType):
    class Meta:
        model = SubjectCategoryModel
