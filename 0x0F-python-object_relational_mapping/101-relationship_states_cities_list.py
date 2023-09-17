#!/usr/bin/python3
"""a script that lists all State objects, and
   corresponding City objects, contained in the
   database passed as argument
"""
if __name__ == "__main__":

    from sqlalchemy import create_engine
    import sys
    from sqlalchemy.orm import Session
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy.schema import Table

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    obj = session.query(State).order_by(State.id).all()
    for states in obj:
        print("{}: {}".format(states.id, states.name))
        for city in states.cities:
            print("    {}: {}".format(city.id, city.name))
    session.close()
