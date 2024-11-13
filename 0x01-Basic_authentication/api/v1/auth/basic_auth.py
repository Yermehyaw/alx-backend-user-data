#!/usr/bin/env python3
"""
Implements BasicAuth in API

Modules imported:

"""
from api.v1.auth.auth import Auth
from models.user import User
import base64
from binascii import Error
from os import getenv
from typing import TypeVar


class BasicAuth(Auth):
    """Holds mthds and variables for BasicAuthentication in the API
    """
    def extract_base64_authorization_header(
            self, authorization_header: str
    ) -> str:
        """Returns the Base64 encoded str in Authorization header"""
        if not isinstance(authorization_header, str):
            return None

        encoded = authorization_header.split()
        if encoded[0] != 'Basic':
            return None
        return encoded[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str
    ) -> str:
        """Returns the decoded Base64 str"""
        if not isinstance(base64_authorization, str):
            return None

        try:
            decoded = base64.b64decode(validate=True)
            decoded = decoded.decode('utf-8')
        except (Error, UnicodeDecodeError):
            return None

        return decoded

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """Return a tuple of extracted user credentials from Auth header"""
        if not isinstance(decoded_base64_authorization_header, str):
            return None

        parsed_credential = decoded_base64_authorization_header.split(':')
        if not parsed_credential:
            return None

        return (parsed_credential[0], parsed_credential[1])

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str
    ) -> TypeVar('User'):
        """Returns an instance of User that matches the credentials"""
        if not user_email or not user_pwd:
            return None

        if not isinstance(user_email, str):
            return None

        if not isinstance(user_pwd, str):
            return None

        user = User(email=user_email, _password=user_pwd)

        # If DB is not empty
        user.load_from_file(User)  # load db to memory
        if user.DATA:
            # Get the user from DB
            found = user.search(User, {'email', user_email})
            if not found:
                return None
        # Validate password credential
        if not found.is_valid_password(user_pwd):
            return None

        return found
            