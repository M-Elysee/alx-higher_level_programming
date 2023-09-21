#!/usr/bin/python3
""" a script that lists all City objects from the database
    passed as argument as well as the user and their password
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from sqlalchemy.schema import Table
from relationship_city import City

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    s = Session(engine)
    for c in s.query(City).order_by(City.id).all():
        print("{}: {} -> {}".format(c.id, c.name, c.state.name))
    s.close()
