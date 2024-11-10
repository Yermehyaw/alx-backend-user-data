#!/usr/bin/env python3
"""
Encrypts and validares user password

Modukes imported: bcrypt

"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Returns a hashed pasword"""
    if not isinstance(password, str):
        raise TypeError
        return

    password = password.encode('utf-8')

    hashed = bcrypt.hashpw(password, bcrypt.gensalt())

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Validates password matches a hash"""
    if not isinstance(password, str):
        raise TypeError
        return

    password = password.encode('utf-8')

    return bcrypt.checkpw(password, hashed_password)
