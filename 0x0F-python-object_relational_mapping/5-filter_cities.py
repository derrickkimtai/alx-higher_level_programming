#!/usr/bin/python3
"""
imported the below modules
"""
import sys
import MySQLdb

def get_state_cities(username, password, database, state_name):
    """
    takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    query = "SELECT cities.name FROM cities INNER JOIN states ON states.id = cities.state_id WHERE states.name LIKE '{:s}%' ORDER BY cities.id ASC".format(state_name)
    cursor.execute(query)

    cities = cursor.fetchall()

    for row in cities:
        print(row)

    db.close()

if __name__ == "__main__":
    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    get_state_cities(username, password, database, state_name)
