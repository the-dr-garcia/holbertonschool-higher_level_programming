#!/usr/bin/python3
"""Defines the City class linked to the cities table."""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """Represents a row of the cities table in a MySQL database."""
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
