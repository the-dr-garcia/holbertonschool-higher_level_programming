#!/usr/bin/python3
"""Changes the name of the State with id = 2 in hbtn_0e_6_usa."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def update_state(username, password, db_name):
    """Change the name of the State with id 2 to New Mexico."""
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, db_name),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    state = session.query(State).filter(State.id == 2).first()
    if state is not None:
        state.name = "New Mexico"
        session.commit()
    session.close()


if __name__ == "__main__":
    update_state(sys.argv[1], sys.argv[2], sys.argv[3])
