#!/usr/bin/env python3
"""Basic authentication.
"""
import re
import base64
import binascii
from typing import Tuple, TypeVar
from .auth import Auth
from models.user import User as User


class BasicAuth(Auth):
    """
    Basic authentication class.
    """
    def extract_base64_authorization_header(
                                            self, authorization_header:
                                            str) -> str:
        """extract base 64 auth head"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None

        token = authorization_header.split(" ")[-1]
        return token

    def decode_base64_authorization_header(
                                            self,
                                            base64_authorization_header:
                                            str) -> str:
        """decode in base 64 auth header."""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            base64.b64decode(base64_authorization_header, validate=True)
            return base64.b64decode(
                    base64_authorization_header,
                    validate=True,
                ).decode('utf-8')
        except (binascii.Error, ValueError):
            return None

    def user_object_from_credentials(
                                    self,
                                    user_email: str, user_pwd:
                                    str) -> TypeVar('User'):
        """user object from credentials"""
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({"email": user_email})
            if not users or users == []:
                return None
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
                return None
        except Exception:
            return None


def current_user(self, request=None) -> TypeVar('User'):
    """
    Returns a User instance based on a received header req
    """
    Auth_header = self.authorization_header(request)
    if Auth_header is not None:
        token = self.extract_base64_authorization_header(Auth_header)
        if token is not None:
            decoded = self.decode_base64_authorization_header(token)
            if decoded is not None:
                email, password = self.extract_user_credentials(decoded)
                if email is not None:
                    return self.user_object_from_credentials(
                                                            email,
                                                            password)
    return
