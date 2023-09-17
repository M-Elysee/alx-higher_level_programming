#!/usr/bin/python3
""" script 14-model_city_fetch_by_state.py that prints
    all City objects from the database hbtn_0e_14_usa
"""
if __name__ == '__main__':

    from sqlalchemy import create_engine
    from model_city import City
    from model_state import State, Base
    import sys
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    s = Session(engine)
    all_obj = s.query(State, City).filter(City.state_id ==
                                          State.id).order_by(City.id).all()
    for st, c in all_obj:
        print('{}: ({}) {}'.format(st.name, c.id, c.name))
    s.close()
