#!/usr/bin/env python3
"""auth
"""
from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> hashpw:
    """function _hash_password
        returns: bytes
        password.encode('utf-8')
        converts the string password to bytes
        as hashpw requires byte input tho.
        """
    salt = gensalt()
    return hashpw(password.encode('utf-8'), salt)
