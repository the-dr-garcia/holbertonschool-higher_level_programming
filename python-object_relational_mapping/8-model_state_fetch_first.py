#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def fetch_first_state(username, password, db_name):
    """Print the State with the lowest id as id: name, or Nothing."""
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, db_name),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    state = session.query(State).order_by(State.id).first()
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
    session.close()


if __name__ == "__main__":
    fetch_first_state(sys.argv[1], sys.argv[2], sys.argv[3])
