#!/usr/bin/python3
"""
    script that takes in the name of a state as an argument and lists
    all cities of that state, using the database hbtn_0e_4_usa
"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(
            host='localhost',
            user=argv[1],
            passwd=argv[2],
            port=3306,
            db=argv[3])
    cur = db.cursor()
    state_name = argv[4]
    cur.execute("SELECT c.name FROM cities as c\
            join states as s on s.id = c.state_id WHERE s.name = %s\
            ORDER BY c.id ASC", (state_name,))
    data = cur.fetchall()
    le = len(data)
    for i, row in enumerate(data):
        if i < le - 1:
            print(row[0], end=', ')
        else:
            print(row[0])
    cur.close()
    db.close()
