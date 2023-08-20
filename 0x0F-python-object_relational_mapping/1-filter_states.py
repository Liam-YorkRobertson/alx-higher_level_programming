#!/usr/bin/python3
"""
    lists all states with name starting with N from database hbtn_0e_0_usa
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()

    cursor.execute("SELECT * FROM `states` WHERE `name` LIKE 'N%' ORDER\
            BY id ASC")
    states = cursor.fetchall()

    unique_states = set()

    for state in states:
        if state[1] not in unique_states:
            unique_states.add(state[1])
            print(state)

    cursor.close()
    db.close()
