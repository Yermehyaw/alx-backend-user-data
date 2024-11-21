#!/usr/bin/env python3
"""
Handles user authentication/authorization protocols

Modules imported:

"""
import bcrypt


class Auth():
    """Authenticates user credentials to enable user log-in

    Attributes:
    None

    """

    def _hash_password(self, password: str) -> bytes:
        """Hashes the users password credential"""

        if not isinstance(password, str):
            return

        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt)
