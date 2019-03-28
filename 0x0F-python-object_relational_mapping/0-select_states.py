#!/usr/bin/python3
"""
Connect to MySQL database using MySQLdb & list all rows
Takes three arguments: MySQL username, MySQL password, database name
"""


import sys
import MySQLdb
if __name__ == "__main__":
    states = MySQLdb.connect(host="127.0.0.1",
                             port=3306,
                             user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3])
    cur = states.cursor()
    cur.execute("SELECT * from states")
    for row in cur.fetchall():
        print("{}".format(row))
