#!/usr/bin/python3
"""  a script that lists all cities from the database hbtn_0e_4_usa
"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute('SELECT cities.id, cities.name, states.name\
              FROM cities INNER JOIN states\
              ON cities.state_id=states.id\
              ORDER BY cities.id ASC')
    row = c.fetchone()
    while (row):
        print(row)
        row = c.fetchone()
