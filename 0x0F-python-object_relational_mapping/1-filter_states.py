#!/usr/bin/python3
"""
script imported
"""
import MySQLdb
import sys

def get_states_starting_with_N(username, password, database):
    """
    lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script_name.py <username> <password> <database>")
    else:
        username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
        get_states_starting_with_N(username, password, database)

