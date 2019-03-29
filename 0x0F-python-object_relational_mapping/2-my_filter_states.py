#!/usr/bin/python3
"""
Connect to MySQL database using MySQLdb & list
all states that match the 4th argument passed

Takes four arguments: MySQL username, MySQL password, database name, state name

This script is not safe from SQL injection.
"""


import sys
import MySQLdb
if __name__ == "__main__":
    states = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3])
    cur = states.cursor()
    cur.execute("SELECT * FROM states \
                WHERE name = '{}' \
                ORDER BY id ASC".format(sys.argv[4]))
    for row in cur.fetchall():
        print("{}".format(row))
    cur.close()
    states.close()
