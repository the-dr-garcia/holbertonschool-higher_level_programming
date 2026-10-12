#!/usr/bin/python3
"""Lists all cities with their state names from the database hbtn_0e_4_usa."""
import MySQLdb
import sys


def cities_by_state(username, password, db_name):
    """Print all cities and their state names, sorted by city id."""
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name "
                "FROM cities JOIN states ON cities.state_id = states.id "
                "ORDER BY cities.id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    cities_by_state(sys.argv[1], sys.argv[2], sys.argv[3])
