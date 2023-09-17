#!/usr/bin/python3
""" a python file that contains the class definition of a
    State and an instance Base = declarative_base()
"""
from sqlalchemy import Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ class that handles state table related"""

    __tablename__ = 'states'
    id = Column(Integer(), unique=True, autoincrement=True,
                primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
