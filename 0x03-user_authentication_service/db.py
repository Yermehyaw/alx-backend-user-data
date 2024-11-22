#!/usr/bin/env python3
"""
SQL Databse class to handle storage and retrieval

Modules imported:


"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

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
        """Databse obj initializer
        """
        self._engine = create_engine('sqlite:///a.db', echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Adds a new user to the database"""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()

        return user

    def find_user_by(self, **kwargs) -> User:
        """Returns a row from the db matching the keyword arg passed"""
        try:
            user = self._session.query(User).filter_by(**kwargs).first()
        except AttributeError:  # invalid keyword in kwargs
            raise InvalidRequestError

        if not user:  # user not found
            raise NoResultFound

        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """Updates a user obj/table in db"""
        user = self.find_user_by(id=user_id)

        for key, value in kwargs.items():
            if key not in User.__table__.columns:
                # Key to be updated isnt an available col/attr in user
                raise ValueError

            setattr(user, key, value)

        self._session.commit()
