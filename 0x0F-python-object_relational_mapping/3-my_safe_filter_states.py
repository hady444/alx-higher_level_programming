#!/usr/bin/python3
"""
    script that takes in an argument and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument
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
    name = argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s\
            ORDER BY id ASC", (name,))
    data = cur.fetchall()
    for row in data:
        print(row)
    cur.close()
    db.close()
