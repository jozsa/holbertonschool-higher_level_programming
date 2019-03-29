#!/usr/bin/python3
"""
This module has one class:
State - inherited from Base.

Base is a declarative base instance from sqlalchemy.
Each instance of State class will be added to
a MySQL database.
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer,
                primary_key=True)
    name = Column(String(128),
                  nullable=False)
