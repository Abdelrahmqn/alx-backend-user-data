#!/usr/bin/env python3
"""auth
"""
from bcrypt import hashpw, gensalt
from db import DB
from user import User
from sqlalchemy.exc import NoResultFound

def _hash_password(password: str) -> bytes:
    """function _hash_password
        returns: bytes
        password.encode('utf-8')
        converts the string password to bytes
        as hashpw requires byte input tho.
        """
    salt = gensalt()
    return hashpw(password.encode('utf-8'), salt)


class Auth:
    """Auth class to interact with the authentication database.
    """
    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        try:
            existing_user = self._db.find_user_by(email=email)
            if existing_user:
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = User(email=email, hashed_password=hashed_password)
            self._db._session.add(new_user)
            self._db._session.commit()

            return new_user
