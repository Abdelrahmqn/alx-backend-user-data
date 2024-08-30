#!/usr/bin/env python3
"""
Hashing
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    hpass
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Vpass
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
