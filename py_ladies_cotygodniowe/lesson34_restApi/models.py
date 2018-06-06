from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer
from sqlalchemy.types import String

from main import db
#
#
# class User(db.Model):
#     """
#     User model for reviewers.
#     """
#     __tablename__ = 'user'
#     id = Column(Integer, autoincrement=True, primary_key=True)
#     active = Column(Boolean, default=True)
#     email = Column(String(200), unique=True)
#     password = Column(String(200), default='')
#     admin = Column(Boolean, default=False)
#
#
# class BlogPosts(db.Model):
#     __tablename__ = 'blogposts'
#     id = Column(Integer, autoincrement=True, primary_key=True)
#     subject = Column(String(200), default='')
#     text = Column(String(5000), default='')


class Product(db.Model):
    __tablename__ = 'product'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(50), default='')
    description = Column(String(200), default='')


class Opinion(db.Model):
    __tablename__ = 'opinion'
    id = Column(Integer, autoincrement=True, primary_key=True)
    author = Column(String(50))
    description = Column(String(200), default='')
    note = Column(Integer)
    product_id = Column(Integer, ForeignKey('product.id'))


class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(50))
    password = Column(String(50))
