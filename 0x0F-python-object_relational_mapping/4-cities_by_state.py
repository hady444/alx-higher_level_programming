#!/usr/bin/python3
"""
    cript that lists all cities from the database hbtn_0e_4_usa
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
    cur.execute("SELECT c.id, c.name, s.name FROM cities as c\
            join states as s on s.id = c.state_id ORDER BY c.id ASC")
    data = cur.fetchall()
    for row in data:
        print(row)
    cur.close()
    db.close()
