#!/usr/bin/python3
"""
imported sys and mysqldb
"""
import sys
import MySQLdb

def get_cities(username, password, database):
    """
     lists all cities from the database hbtn_0e_4_usa
     """
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor= db.cursor()

    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    cursor.execute(query)

    cities = cursor.fetchall()

    for city in cities:
        print(city)

    db.close

if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    get_cities(username, password, database)
