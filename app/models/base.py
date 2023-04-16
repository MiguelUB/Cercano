"""
This file has common attributes that all the models share.
"""

import typing as t

from sqlalchemy import BigInteger, Boolean, Column, DateTime
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.sql import func

class_registry: t.Dict = {}


@as_declarative(class_registry=class_registry)
class Base(object):
    """
    Base class is an object that creates the columns for the shared attributes
    of the other models, as the id, when it was created, updated or deleted and if
    the account is active.
    """

    id: t.Any
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower()

    # Shared columns in all tables
    @declared_attr
    def id(self):
        return Column(BigInteger, primary_key=True, index=True)

    def __repr__(self):
        return "<id {}>".format(self.id)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now(), default=func.now())
    deleted_at = Column(DateTime, nullable=True)
    active = Column(Boolean, default=True)
