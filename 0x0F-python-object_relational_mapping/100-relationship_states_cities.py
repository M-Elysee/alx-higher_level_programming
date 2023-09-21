#!/usr/bin/python3
"""a script that creates the State “California” with
   the City “San Francisco” from the database passed in
   the command line as well as the user and password
"""
from relationship_state import Base, State
from sqlalchemy import create_engine
from relationship_city import City
from sqlalchemy.orm import Session
from sqlalchemy.schema import Table
import sys

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    s = Session(engine)
    city_obj = City(name='San Francisco')
    state_obj = State(name='California')
    state_obj.cities.append(city_obj)
    s.add_all([state_obj, city_obj])
    s.commit()
    s.close()
