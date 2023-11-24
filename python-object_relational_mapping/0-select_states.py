#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys
# Connect to MySQL database
db = MySQLdb.connect(host="localhost", port=3306,
                     user=sys.argv[1], password=sys.argv[2], db=sys.argv[3])

# Create cursor to execute queries and use dictionary format
cur = db.cursor()

# Execute query to select all states from database
cur.execute("SELECT states.id, states.name FROM states ORDER BY states.id ASC")

# Fetch all the rows in a list of lists
rows = cur.fetchall()
for row in rows:
    print(row)

# Close all cursors and connection
cur.close()
db.close()
