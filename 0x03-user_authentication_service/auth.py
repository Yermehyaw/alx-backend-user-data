#!/usr/bin/env python3
"""
Handles user authentication/authorization protocols

Modules imported:

"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    """Hashes the users password credential"""
    if not isinstance(password, str):
        return
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def _generate_uuid() -> str:
    """Generates uniques user ids"""
    return str(uuid4().int)


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
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            # user dosent exist in db, create new user
            hashed = _hash_password(password)
            new_user = self._db.add_user(email, hashed)
            return new_user

        if user:  # user already exists
            raise ValueError(f'User {email} already exists')

    def valid_login(self, email: str, password: str) -> bool:
        """Ensures user login credentials are valid"""
        if not isinstance(email, str) or not isinstance(password, str):
            return False

        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        if not user:
            return False

        return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password)
