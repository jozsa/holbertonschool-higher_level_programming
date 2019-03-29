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
    """
    This class is linked to the states table.

    Attributes:
        id: Integer, required, primary key
        name: String, required
    """
    __tablename__ = 'states'

    id = Column(Integer,
                primary_key=True)
    name = Column(String(128),
                  nullable=False)
