#!/usr/bin/env python3
"""
Authorization for API

modules imported: flask.request, typing.TypeVar

"""
from flask import request
from typing import TypeVar


class Auth:
    """Authorization class

    Attributes:
    None
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if client auth is required"""
        return False

    def authorization_header(self, request=None) -> str:
        """Gets the request header from a request obj"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns the current client"""
        return None
