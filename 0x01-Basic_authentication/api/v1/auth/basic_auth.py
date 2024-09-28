#!/usr/bin/env python3
"""Basic authentication.
"""
import re
import base64
import binascii
from typing import Tuple, TypeVar
from .auth import Auth
from models.user import User


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
