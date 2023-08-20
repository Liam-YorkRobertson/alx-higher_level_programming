#!/usr/bin/python3
"""
Script that lists all states with a name starting with 'N' (uppercase)
from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()

    cursor.execute("SELECT * FROM `states` WHERE `name` \
            LIKE 'N%' ORDER BY id ASC LIMIT 2")

    [print(state) for state in cursor.fetchall()]

    cursor.close()
    db.close()
