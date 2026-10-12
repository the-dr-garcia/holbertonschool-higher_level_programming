#!/usr/bin/python3
"""Deletes all State objects containing the letter a from hbtn_0e_6_usa."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def delete_states_with_a(username, password, db_name):
    """Delete every State whose name contains the letter a."""
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, db_name),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    for state in session.query(State).filter(
            State.name.like("%a%")).all():
        session.delete(state)
    session.commit()
    session.close()


if __name__ == "__main__":
    delete_states_with_a(sys.argv[1], sys.argv[2], sys.argv[3])
