import graphene as gph

from bestiary.apps.subject.api.types import *


class SubjectQuery(object):
    subjects = gph.List(lambda: Subject)
    subject_by_id = gph.Field(lambda: Subject, subject_id=gph.Int())
    search_subjects = gph.List(lambda: Subject, query_string=gph.String())

    def resolve_subjects(self, info):
        return SubjectModel.query.all()

    def resolve_subject_by_id(self, info, subject_id):
        return SubjectModel.query.get(subject_id)

    def resolve_search_subjects(self, info, query_string):
        return SubjectModel.query.whooshee_search(query_string).all()
