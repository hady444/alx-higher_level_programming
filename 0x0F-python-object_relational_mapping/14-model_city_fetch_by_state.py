#!/usr/bin/python3
"""
    script that adds the State object “Louisiana” to the database
    hbtn_0e_6_usa
"""

from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(State, City).filter(State.id == City.state_id)

    for ci in cities:
        print("{}: ({}) {}".format(ci.State.name, ci.City.id, ci.City.name))
    session.close()
