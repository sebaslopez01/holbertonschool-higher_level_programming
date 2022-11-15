#!/usr/bin/python3

"""
This script lists all states from a database
"""


if __name__ == '__main__':
    import MySQLdb
    import sys

    username, password, database_name = sys.argv[1:]

    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=database_name)
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id")
    rows = cur.fetchall()

    for row in rows:
        print(row)
