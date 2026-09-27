#!/usr/bin/env python3
"""Module for serializing/deserializing custom objects using pickle."""
import pickle


class CustomObject:
    """Represent a custom object with name, age and student status."""

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject instance."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current instance and save it to a file."""
        try:
            with open(filename, mode="wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load and return an instance from a serialized file."""
        try:
            with open(filename, mode="rb") as f:
                return pickle.load(f)
        except Exception:
            return None
