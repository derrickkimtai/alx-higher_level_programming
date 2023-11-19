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

    query = """
        SELECT cities.id, cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    cities = cursor.fetchall()

    for city in cities:
        print(city)

    db.close()

if __name__ == "__main__":
    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    get_state_cities(username, password, database, state_name)
