#!/usr/bin/python3
"""Prints the id of the State matching a name given as an argument."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_state(username, password, db_name, state_name):
    """Print the id of the State named state_name, or Not found."""
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, db_name),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    state = session.query(State).filter(State.name == state_name).first()
    if state is None:
        print("Not found")
    else:
        print(state.id)
    session.close()


if __name__ == "__main__":
    get_state(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
