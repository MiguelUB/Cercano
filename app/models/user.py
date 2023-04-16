from sqlalchemy import Column, DateTime, Integer, String

from app.models.base import Base
from config.db import db


class User(Base, db.Model):
    """
    This user class inherits from the base file some common columns for auditors,
    in addition to those in this file also is  contained basic user information for authentication.
    """

    __tablename__ = "user"

    username = Column(String(100), unique=False, nullable=False)
    profile_name = Column(String(100), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(25), unique=True, nullable=False)
    avatar_img = Column(String(100), unique=False, nullable=False)
    # likes
    # bussines
