from slugify import slugify
from sqlalchemy.ext.hybrid import hybrid_property

from app import db
from apps.user.models import User

class SubjectType(db.Model):
    __tablename__ = "subject_types"

    name = db.Column(db.String(255), nullable=False)
    _slug = db.Column("slug", db.String(255), nullable=False)

    @hybrid_property
    def slug(self) -> str:
        return self._slug

    @slug.setter
    def slug(self, value: str) -> None:
        self._slug = slugify(value)


class SubjectCategory(db.Model):
    __tablename__ = "subject_categories"

    name = db.Column(db.String(255), nullable=False)
    _slug = db.Column("slug", db.String(255), nullable=False)
    about = db.Column(db.Text)

    @hybrid_property
    def slug(self) -> str:
        return self._slug

    @slug.setter
    def slug(self, value: str) -> None:
        self._slug = slugify(value)


class Subject(db.Model):
    __tablename__ = "subjects"

    type_id = db.Column(db.Integer, db.ForeignKey(SubjectType.id), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey(SubjectCategory.id), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    name = db.Column(db.String(255), nullable=False)
    about = db.Column(db.Text, nullable=False)
    habitat = db.Column(db.String(255), nullable=False)

    type = db.relationship(SubjectType)
    category = db.relationship(SubjectCategory)
    user = db.relationship(User)
