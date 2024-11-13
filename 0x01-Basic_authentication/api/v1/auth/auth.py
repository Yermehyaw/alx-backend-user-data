#!/usr/bin/env python3
"""
Authorization for API

modules imported: flask.request, typing.TypeVar

"""
from flask import (
    request,
    Request,
)
from typing import (
    Optional,
    TypeVar,
    List,
)
import re


class Auth:
    """Authorization class

    Attributes:
    None
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if client auth is required"""
        if not path or not excluded_paths:
            return True

        last_char_pattern = r"/$"
        if not re.search(last_char_pattern, path):
            # if the last char isnt a '/'
            path = path + '/'

        if path not in excluded_paths:
            return True

        return False

    def authorization_header(self, request: Request = None) -> Optional[str]:
        """Gets the request header from a request obj"""
        return None

    def current_user(self, request: Request = None) -> TypeVar('User'):
        """Returns the current client"""
        return None
