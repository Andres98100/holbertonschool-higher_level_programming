#!/usr/bin/python3
"""
display the cities and state
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306, user=username,
        passwd=password, db=database,
        charset="utf8")

    cur = conn.cursor()
    cur.execute("SELECT c.id, c.name, st.name \
                FROM cities AS c \
                JOIN states AS st \
                    ON c.state_id = st.id \
                ORDER BY id")
    querty_rows = cur.fetchall()
    for row in querty_rows:
        print(row)
    cur.close()
    conn.close()
