#!/usr/bin/python3

"""
This script lists all values in the states where name matches the argument
"""


if __name__ == '__main__':
    import MySQLdb
    import sys

    username, password, database_name, state_name = sys.argv[1:]

    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=database_name)
    cur = db.cursor()

    cur.execute("""SELECT * FROM states
    WHERE name LIKE BINARY '{}'
    ORDER BY id""".format(state_name))
    rows = cur.fetchall()

    for row in rows:
        print(row)
