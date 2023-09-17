#!/usr/bin/python3
""" a script that lists all states with a name starting with
   N (upper N) from the database , user, and password passed as argument
"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute('SELECT id, name FROM states WHERE name\
              LIKE "N%" ORDER BY states.id ASC')
    row = c.fetchone()
    while (row):
        print(row)
        row = c.fetchone()
