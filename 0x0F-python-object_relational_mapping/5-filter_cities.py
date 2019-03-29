#!/usr/bin/python3
"""
Connect to MySQL database using MySQLdb &
print all cities in state passed as 4th argument

Takes 4 arguments: MySQL username, MySQL password, database name, state name
"""


import sys
import MySQLdb
if __name__ == "__main__":
    usa_db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3])
    cur = usa_db.cursor()
    cur.execute("SELECT cities.name \
                FROM cities \
                JOIN states ON (cities.state_id = states.id) \
                WHERE states.name = '{}' \
                ORDER BY cities.id ASC"
                .format(sys.argv[4]))
    citystring = ', '.join([row[0] for row in cur.fetchall()])
    print(citystring)
    cur.close()
    usa_db.close()
