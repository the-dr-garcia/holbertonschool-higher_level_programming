#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa."""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def fetch_cities_by_state(username, password, db_name):
    """Print all cities as state name: (city id) city name, by city id."""
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, db_name),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    for city, state in session.query(City, State).filter(
            City.state_id == State.id).order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()


if __name__ == "__main__":
    fetch_cities_by_state(sys.argv[1], sys.argv[2], sys.argv[3])
