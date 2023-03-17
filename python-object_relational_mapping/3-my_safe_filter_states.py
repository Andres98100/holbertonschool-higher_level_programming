#!/usr/bin/python3
"""
displays the values of the table passed as an argument
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    matchName = sys.argv[4].split(';')[0].strip("'")

    conn = MySQLdb.connect(
        host="localhost",
        port=3306, user=username,
        passwd=password, db=database,
        charset="utf8")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM states WHERE name LIKE '{matchName}'")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
