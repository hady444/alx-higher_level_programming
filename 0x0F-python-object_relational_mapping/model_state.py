#!/usr/bin/python3
"""
    class definition of a State and an instance Base = declarative_base()
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()


class State(Base):
    """
        inherits from Base links to the MySQL table states
        
        Attributes:
            id (int): that represents a column of an auto-generated, unique integer
            name (string): that represents a column of a string
    """
    __tablename__ = 'state'
    id = Column(INTEGER, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
