#!/usr/bin/env python3
"""
SQL Databse class to handle storage and retrieval

Modules imported:


"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from typing import TypeVar

from user import Base
from user import User


class DB:
    """
    Database class to handle database sessions: session creation,
    commits and session closes

    Attributes:
    self._engine: databse engine(sqlite)
    self.__session: current databse session

    """
    def __init__(self):
        """Databse obj initializer"""
        self._engine = create_engine('sqlite:///a.db', echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        Returns the current session of the DB
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> TypeVar('User'):
        """Adds a new user to the database"""
        current_session = self._session  # creates/rets a session
        user = User(email=email, hashed_password=hashed_password)
        current_session.add(user)
        current_session.commit()

        return user
