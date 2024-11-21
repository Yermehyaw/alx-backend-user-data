#!/usr/bin/env python3
"""
User model. A User clas sto describe what a user obj is in the DB

Modules imported: sqlalchemy, bcrypt
bcrypt: Encrypts user login
sqlalchemy: maps model to a DB instance


"""
import bcrypt
from sqlalchemy import (
    Column,
    Integer,
    String
)
from sqlalchemy.ext.declarative import declarative_base
from typing import (
    List,
)


Base = declarative_base()


class User(Base):
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

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250))
    reset_token = Column(String(250))

    """
    def __init__(self, email: str, password: str) -> None:
        Class obj initializer
        if not isinstance(email, str) or not isinstance(password, str):
            return

        self.email = email

        salt = bcrypt.gensalt()
        self.hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

        self.session_id = None

        self.reset_token = None
        """
