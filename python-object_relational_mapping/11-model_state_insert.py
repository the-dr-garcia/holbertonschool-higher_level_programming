#!/usr/bin/python3
"""Adds the State object Louisiana to the database hbtn_0e_6_usa."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def insert_state(username, password, db_name):
    """Add the state Louisiana to the database and print its new id."""
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, db_name),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(new_state.id)
    session.close()


if __name__ == "__main__":
    insert_state(sys.argv[1], sys.argv[2], sys.argv[3])
