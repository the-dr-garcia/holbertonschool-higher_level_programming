#!/usr/bin/python3
"""Lists all State objects containing the letter a from hbtn_0e_6_usa."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def filter_states_with_a(username, password, db_name):
    """Print all State objects whose name contains a, sorted by id."""
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, db_name),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    for state in session.query(State).filter(
            State.name.like("%a%")).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()


if __name__ == "__main__":
    filter_states_with_a(sys.argv[1], sys.argv[2], sys.argv[3])
