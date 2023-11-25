#!/usr/bin/python3
""" a script that takes in an argument
and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument."""

import MySQLdb
import sys

if __name__ == "__main__":
    """Connect to the dabatabase"""
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])

    """Create a cursor object"""
    cur = db.cursor()

    """get the state name """
    state_name = sys.argv[4]

    """acreate the query"""
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY states.id ASC".fortmat(
        state_name)

    """Execute the query"""
    cur.execute(query)

    """Fetch all rows"""
    for row in cur.fetchall():
        print(row)

    """Close cursor and db"""
    cur.close()
    db.close()
