#!/usr/bin/env python3
"""
User model. A User clas sto describe what a user obj is in the DB

Modules imported: sqlalchemy, bcrypt
bcrypt: Encrypts user login
sqlalchemy: maps model to a DB instance
uuid: generates unique ids


"""
import bcrypt
from sqlalchemy import (
    Column,
    Integer,
    String
)
from typing import (
    List,
)
from uuid import uuid4


class User():
    """
    Describes a user obj

    Attributes:
    id(int): unique id of user
    email(str): email str of user
    hashed_password(str): encrypted pword
    session_id(str): unique session id
    reset_token(str): token for user's session
    """
    __tablename__ = 'users'

    class __table__():
        """Defines the SQL DB table coulmns

        Attributes:
        id(int): primary key, unique id of user
        email(str): Nonnullable, email str of user
        hashed_password(str): Non-nullable, encrypted pword
        session_id(str): NNUL, unique session id
        reset_token(str): NNUL, token for user's session
        """
        users = User()
        users.id = Column(Integer, primary_key=True)
        users.email = Column(String, nullable=False)
        users.hashed_password = Column(String, nullable=False)
        users.session_id = Column(String, nullable=False)
        users.reset_token = Column(String, nullable=False)
        columns = [
            users.id,
            users.email,
            users.hashed_paswword,
            users.session_id,
            users.reset_token,
        ]

    def __init__(self, email: str, password: str) -> None:
        """Class obj initializer
        """
        if not isinstance(email, str) or not isinstance(password, str):
            return

        self.id = uuid4().int

        self.email = email

        salt = bcrypt.gensalt()
        self.hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

        self.session_id = None

        self.reset_token = None
