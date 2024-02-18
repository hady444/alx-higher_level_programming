#!/usr/bin/python3
"""
    script that lists all State objects from the database hbtn_0e_6_usa.
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

engine = create_engine(f'mysql+mysqlconnector://{sys.argv[1]}:{sys.argv[2]}\
        @localhost:3306/{sys.argv[3]}')
try:
    engine.connect()
except e:
    print("Connection error", e)

Session = sessionmaker(bind=engine)
session = Session()
for row in session.query(State).order_by(State.id).all():
    print(f'{State.id}: {State.name}')
