#!/usr/bin/env python3
"""Module for basic serialization/deserialization of data using JSON."""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary to JSON and save it to a file."""
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load and deserialize JSON data from a file into a dictionary."""
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
