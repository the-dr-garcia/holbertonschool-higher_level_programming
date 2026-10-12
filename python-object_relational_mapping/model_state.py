#!/usr/bin/python3
"""Defines the State class and the Base instance for SQLAlchemy."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a row of the states table in a MySQL database."""
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
