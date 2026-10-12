#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa."""
import MySQLdb
import sys


def list_states(username, password, db_name):
    """Print all states sorted by id in ascending order."""
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    list_states(sys.argv[1], sys.argv[2], sys.argv[3])
