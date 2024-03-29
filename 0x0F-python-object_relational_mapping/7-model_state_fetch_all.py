#!/usr/bin/python3
""" a script that lists all State objects from the database hbtn_0e_6_usa """
if __name__ == '__main__':

    from sqlalchemy import create_engine
    from model_state import State, Base
    import sys
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    s = Session(engine)
    for states in s.query(State).order_by(State.id).all():
        print('{}: {}'.format(states.id, states.name))
    s.close()
