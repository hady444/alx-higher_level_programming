#!/usr/bin/python3
"""
    script that deletes all State objects with a name containing
    the letter a from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()
    delete_states = session.query(State).filter(State.name.like('%a%')).all()
    for state in delete_states:
        session.delete(state)
    session.commit()

    session.close()
