#!/usr/bin/python3
"""
import sys and mysql
"""
import sys
import MySQLdb

def get_match_arg(username, password, database, state_name):
    """
    a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections!
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    results = cursor.fetchall()
    for row in results:
        print(row)
    db.close()

if __name__ == "__main__":
    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    get_match_arg(username, password, database, state_name)
