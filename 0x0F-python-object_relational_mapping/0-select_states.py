#!/usr/bin/python3
""" a script that lists all states from the database hbtn_0e_0_usa """

if __name__ == '__main__':
    import MySQLdb
    import sys
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute('SELECT id, name FROM states ORDER BY states.id ASC')
    row = c.fetchone()
    while (row):
        print(row)
        row = c.fetchone()
