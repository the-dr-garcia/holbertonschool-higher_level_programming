#!/usr/bin/python3
"""Lists all states with a name starting with N from hbtn_0e_0_usa."""
import MySQLdb
import sys


def filter_states(username, password, db_name):
    """Print all states starting with N, sorted by id in ascending order."""
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' "
                "ORDER BY id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    filter_states(sys.argv[1], sys.argv[2], sys.argv[3])
