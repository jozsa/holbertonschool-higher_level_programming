#!/usr/bin/python3
"""
Connect to MySQL database using MySQLdb & list all states that start with N
Takes three arguments: MySQL username, MySQL password, database name
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
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cur.fetchall():
        if row[1][0] == 'N':
            print("{}".format(row))
    cur.close()
    states.close()
