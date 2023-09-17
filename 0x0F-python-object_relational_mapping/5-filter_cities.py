#!/usr/bin/python3
"""  a script that takes in the name of a state as an argument
     and lists all cities of that state, using the database hbtn_0e_4_usa
"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute('SELECT cities.name FROM cities WHERE cities.state_id\
              =(SELECT states.id FROM states WHERE states.name="{}")'.
              format(sys.argv[4]))
    row = c.fetchall()
    if not row:
        print()
    for r in row:
        if r != row[-1]:
            print('{}'.format(r[0]), end=", ")
        else:
            print('{}'.format(r[0]))
