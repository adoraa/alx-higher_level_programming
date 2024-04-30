#!/usr/bin/python3
"""
Displays all values in the states table where name matches the argument.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    state_name = sys.argv[4]
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
                ORDER BY states.id ASC".format(state_name,))
    row = cursor.fetchall()
    for row in rows:
        print(row)
