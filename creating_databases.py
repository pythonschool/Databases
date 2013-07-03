#03-07-2013
#creating a new database with SQLite3

import sqlite3

def create_database(db_name):
    with sqlite3.connect(db_name) as db:
        print("new database called {0} created".format(db_name))

if __name__ == "__main__":
    name = input("Please enter the name of the database you wish to create: ")
    create_database(name)