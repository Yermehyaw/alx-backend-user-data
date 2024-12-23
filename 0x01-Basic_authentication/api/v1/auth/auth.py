#!/usr/bin/env python3
"""
Authorization for API

modules imported: flask.request, typing, TypeVar

"""
from flask import (
    request,
)
from models.user import User
from typing import (
    Optional,
    TypeVar,
    List,
)
import re


class Auth:
    """Authorization class

    Attributes:
    require_path(): Returns true if a request to a path needs
    authentication
    authorization_header(): Returns the value present in the
    Authorization i the request header
    current_user(): Verifies if a client is logged in
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns true if the path does NOT require auth"""
        if not path or not excluded_paths:
            return True

        last_char_pattern = r"/$"
        if not re.search(last_char_pattern, path):
            # if the last char isnt a '/'
            path = path + '/'

        if path in excluded_paths:
            return True

        return False

    def authorization_header(self, request=None) -> Optional[str]:
        """Gets the request header from a request obj"""
        if not request:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns the current client"""
        return None
