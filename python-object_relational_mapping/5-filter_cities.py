#!/usr/bin/python3
"""a script that takes in the name
of a state as an argument and lists
all cities of that state, using the
database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """Connect to the database"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])

    """Create a cursor object"""
    cur = db.cursor()

    # Create query
    query = "SELECT cities.name FROM citites WHERE state.name = %s\
            ORDER BY cities.id ASC"

    """Execute the query"""
    cur.execute(query, (sys.argv[4],))

    """Fetch all rows"""
    for row in cur.fetchall():
        print(row)

    """Close cursor and db"""
    cur.close()
    db.close()
