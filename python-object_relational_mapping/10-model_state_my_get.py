#!/usr/bin/python3
"""
show state like args
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    matchname = sys.argv[4].split(";")[0].strip("'")

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database, matchname),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name == matchname).first()

    if states:
        print(states.id)
    else:
        print("Not found")

    session.close()
