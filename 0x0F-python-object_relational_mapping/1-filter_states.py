#!/usr/bin/python3
"""
Script that lists all states with a name starting with 'N' (uppercase)
from the database hbtn_0e_0_usa.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `states` ORDER BY `id`")

    for state in cursor.fetchall():
        if state[1][0] == "N":
            print(state)
