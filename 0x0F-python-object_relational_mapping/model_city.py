#!/usr/bin/python3
"""

"""


from sqlalchemy import Base, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from models
Base = declarative_base()
class City(Base):
    __table_name__ = 'cities'
    id = Column(Integer, autincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
