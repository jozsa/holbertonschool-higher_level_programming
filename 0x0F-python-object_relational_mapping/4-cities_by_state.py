#!/usr/bin/python3
"""
Connect to MySQL database using MySQLdb & list all rows in passed database

Takes three arguments: MySQL username, MySQL password, database name
"""


import sys
import MySQLdb
if __name__ == "__main__":
    usa_db = MySQLdb.connect(host="127.0.0.1",
                             port=3306,
                             user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3])
    cur = usa_db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
                FROM cities \
                JOIN states ON (cities.state_id = states.id)")
    for row in cur.fetchall():
        print("{}".format(row))
    cur.close()
    usa_db.close()
