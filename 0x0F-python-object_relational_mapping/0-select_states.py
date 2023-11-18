import MYSQLdb
import sys

def getstates(username, password, database):
    db = MYSQLdb.connect(host="localhost", port=3306, user=kimtai, passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    row = cursor.fetchall()
    for row in rows:
        print(row)

    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python 0-select_states.py <username> <password> <database>")
    else:
        username, password, database = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[3]
        get_states(username, password, database)
