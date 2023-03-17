#!/usr/bin/python3
"""
display cities
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
    cur.execute("SELECT c.name \
                FROM cities AS c \
                JOIN states AS st \
                    ON c.state_id = st.id \
                WHERE st.name = '{}' ORDER BY c.id".format(matchName))
    querty_rows = cur.fetchall()
    finish = 0
    for row in querty_rows:
        if finish > 0:
            print(", ", end="")
        print(row[0], end="")
        finish += 1
    print()
    cur.close()
    conn.close()
