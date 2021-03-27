#!/usr/bin/python3
import MySQLdb
from sys import argv
###

###
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port = 3306)
    cur = db.cursor()
    cur.execute("SELECT cities.name, states.name FROM cities, states\
    WHERE cities.state_id=states.id AND states.name=%s\
    ORDER BY cities.id ASC", (argv[4],))
    rows = cur.fetchall()
    tup = []
    for city in rows:
        tup.append(city[0])
    print(", ".join(tup))
    # Close all cursors
    cur.close()
    # Close all databases
    db.close()