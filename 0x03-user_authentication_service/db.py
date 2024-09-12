#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from user import User, Base
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
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
        """add user.email, hashed_pass elements
        """

        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """finding users in database
        Args:
            kwargs (str): The user.
        Returns:
            User: The created User object.
        """
        for element in kwargs:
            if not hasattr(User, element):
                raise InvalidRequestError
            usr = self._session.query(User).filter_by(**kwargs).first()
            if not usr:
                raise NoResultFound
            return usr

    def update_user(self, user_id: int, **kwargs) -> None:
        """find user and update key with value
        """
        find_user = DB.find_user_by(id=user_id)
        for key, value in kwargs.item():
            if not hasattr(find_user, key):
                raise ValueError(f"{key} not valid")
            setattr(find_user, key, value)
        self._session.commit()
