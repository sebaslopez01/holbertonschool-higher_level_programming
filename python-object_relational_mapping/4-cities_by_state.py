#!/usr/bin/python3

"""
This script lists all cities
"""


if __name__ == '__main__':
    import MySQLdb
    import sys

    username, password, database_name = sys.argv[1:]

    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=database_name)
    cur = db.cursor()

    cur.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        LEFT JOIN states
        ON cities.state_id = states.id
        ORDER BY cities.id
    """)
    rows = cur.fetchall()

    for row in rows:
        print(row)
