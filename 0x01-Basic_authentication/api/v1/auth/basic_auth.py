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
    pass
