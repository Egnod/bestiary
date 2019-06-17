from typing import Union

from bestiary.app.models import User


def authenticate(username: str, password: str) -> Union[None, User]:
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user


def identity(payload: dict) -> User:
    user_id = payload["identity"]

    return User.query.get(user_id)
