from slugify import slugify
from sqlalchemy.ext.hybrid import hybrid_property

from app import db
from passlib.hash import argon2


class UserDetail(db.Model):
    __tablename__ = "users_details"

    first_name = db.Column(db.String(255), nullable=False)
    about = db.Column(db.Text)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))


class User(db.Model):
    __tablename__ = "users"

    _login = db.Column("login", db.String(255), nullable=False)
    _password_hash = db.Column("password_hash", db.String(255), nullable=False)

    detail = db.relationship(UserDetail)

    @hybrid_property
    def login(self) -> str:
        return self._login

    @login.setter
    def login(self, value: str) -> None:
        self._login = slugify(value)

    @hybrid_property
    def password_hash(self) -> str:
        return self._password_hash

    @password_hash.setter
    def password_hash(self, value: str) -> None:
        self._password_hash = argon2.hash(value)
