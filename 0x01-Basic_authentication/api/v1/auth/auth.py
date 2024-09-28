#!/usr/bin/env python3
""" auth file
"""
from flask import request
from typing import List, TypeVar

User = TypeVar('User')


class Auth:
    """Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        returns False - path and excluded_paths
        """
        if path is None:
            return True

        if not excluded_paths or len(excluded_paths) == 0:
            return True
        if not path.endswith('/'):
            path += '/'
        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        returns None - request
        """
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar("User"): # type: ignore
        """
        None - request
        """
        return None
