#!/usr/bin/python3
"""
    script that lists all states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa
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
    cur.execute("SELECT * FROM states\
                    WHERE name LIKE BINARY 'N%'\
                    ORDER BY id ASC")
    data = cur.fetchall()
    for row in data:
        print(row)
    cur.close()
    db.close()
