#!/usr/bin/python3
"""
    script that lists all State objects from the database hbtn_0e_6_usa.
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
    sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
Session = sessionmaker(bind=engine)
session = Session()
for row in session.query(State).order_by(State.id).all():
    print(f'{State.id}: {State.name}')
session.close()
