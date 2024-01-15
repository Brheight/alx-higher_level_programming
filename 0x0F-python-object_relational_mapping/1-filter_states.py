#!/usr/bin/python3

"""
This script lists all states with names starting with 'N' (upper N) from the hbtn_0e_0_usa database.

Usage:
    ./1-filter_states.py <mysql_username> <mysql_password> <database_name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
