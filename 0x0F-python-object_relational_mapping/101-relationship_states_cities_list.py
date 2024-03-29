#!/usr/bin/python3
"""a script that lists all State objects, and
   corresponding City objects, contained in the
   database passed as argument
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
import sys
from relationship_city import City
from sqlalchemy.schema import Table

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    s = Session(engine)
    obj = s.query(State).order_by(State.id).all()
    for o in obj:
        print("{}: {}".format(o.id, o.name))
        for city in o.cities:
            print("    {}: {}".format(city.id, city.name))
    s.close()
