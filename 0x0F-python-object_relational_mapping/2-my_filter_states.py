#!/usr/bin/python3
"""
sys and mysql was imported 
"""
import sys
import MySQLdb

def get_states_by_name(username, password, database, state_name):
    """ takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cursor.execute(query) 
    results = cursor.fetchall()
    for row in results:
        print(row)
    db.close()

if __name__ == "__main__":
    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    get_states_by_name(username, password, database, state_name)
