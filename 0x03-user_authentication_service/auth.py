#!/usr/bin/env python3
"""
Handles user authentication/authorization protocols

Modules imported:

"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Hashes the users password credential"""
    if not isinstance(password, str):
        return
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


class Auth:
    """Auth class to interact with the authentication database.

    Attributes:
    _db: Database with database session, storage & retrieval mthds
    """
    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a new user into the database, provided
        the credentiaks dont belong to any prev user
        """
        if not isinstance(email, str):
            return

        try:
            user = self._db.find_user_by(
                email=email,
                hashed_password=password
            )
        except NoResultFound:
            # user dosent exist in db, create new user
            hashed = _hash_password(password)
            new_user = self._db.add_user(email, hashed)
            return new_user

        if user:  # user already exists
            raise ValueError(f'User {email} already exists')
