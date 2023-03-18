#!/usr/bin/python3
"""
change a state
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_query = session.query(State).filter_by(id=2).first()
    state_query.name = 'New Mexico'
    session.commit()

    states = session.query(State).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
