import graphene as gph
from flask_jwt import jwt_required, current_identity

from bestiary.apps.subject.api.types import *
from bestiary.app import db


class CreateSubject(gph.Mutation):
    class Arguments:
        name = gph.String(required=True)
        about = gph.String(required=True)

        type_id = gph.ID(required=True)
        category_id = gph.ID(required=True)

    subject = gph.Field(Subject)

    @staticmethod
    @jwt_required()
    def mutate(root, info, name, about, type_id, category_id):
        subject = SubjectModel()
        subject.name = name
        subject.about = about

        subject.type_id = type_id
        subject.category_id = category_id
        subject.user_id = current_identity.id

        db.session.add(subject)
        db.session.commit()

        return CreateSubject(subject=subject)


class EditSubject(gph.Mutation):
    class Arguments:
        name = gph.String()
        about = gph.String()

        type_id = gph.ID()
        category_id = gph.ID()

        subject_id = gph.ID(required=True)

    subject = gph.Field(Subject)

    @staticmethod
    @jwt_required()
    def mutate(root, info, subject_id, **fields):

        subject = SubjectModel.query.filter_by(id=subject_id)

        if not subject.first() or current_identity.id != subject.first().user_id:
            return None

        subject.update(fields)

        db.session.commit()

        return EditSubject(subject=subject.first())
