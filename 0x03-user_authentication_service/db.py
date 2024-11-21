#!/usr/bin/env python3
"""
SQL Databse class to handle storage and retrieval

Modules imported:


"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

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
        self._engine = create_engine('sqlite:///a.db', echo=True)
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

    def add_user(self, email: str, hashed_password: str) -> None:
        """Adds a new user to the database"""
        if not self.__session:
            # if no active session, call session creator
            self._session  # a prpty mthd that creates a sessiom

        if not isinstance(email, str) or not isinstance(hashed_password, str):
            return

        user = User()
        user.email = email
        user.hashed_password = hashed_password

        self.__session.add(user)
        self.__session.commit()

        return user
