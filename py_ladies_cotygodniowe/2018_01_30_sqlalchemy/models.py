from sqlalchemy import Column
from sqlalchemy.types import Integer
from sqlalchemy.types import String
from sqlalchemy.types import Boolean

from main import db


class User(db.Model):
    """
    User model for reviewers.
    """
    __tablename__ = 'user'
    id = Column(Integer, autoincrement=True, primary_key=True)
    active = Column(Boolean, default=True)
    email = Column(String(200), unique=True)
    password = Column(String(200), default='')
    admin = Column(Boolean, default=False)


class BlogPosts(db.Model):
    __tablename__ = 'blogposts'
    id = Column(Integer, autoincrement=True, primary_key=True)
    subject = Column(String(200), default='')
    text = Column(String(5000), default='')
