#!/usr/bin/python3
"""Displays all states matching a name given as an argument, safely."""
import MySQLdb
import sys


def my_safe_filter_states(username, password, db_name, state_name):
    """Print all states matching state_name using a parameterized query."""
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                (state_name,))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    my_safe_filter_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
