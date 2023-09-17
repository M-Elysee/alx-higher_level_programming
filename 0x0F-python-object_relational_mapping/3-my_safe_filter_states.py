#!/usr/bin/python3
"""  a script that takes in an argument and displays all
     values in the states table of h   btn_0e_0_usa where
     name matches the argument. the database , user, and
     password are passed as argument safe form sql injection
"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
        passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute('SELECT id, name FROM states WHERE name=%s ORDER BY states.id ASC', (sys.argv[4],))
    row = c.fetchone()
    while (row):
        print(row)
        row = c.fetchone()
