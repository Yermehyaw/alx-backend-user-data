#!/usr/bin/env python3
"""
Handles user authentication/authorization protocols

Modules imported:

"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hashes the users password credential"""
    if not isinstance(password, str):
            return
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)
