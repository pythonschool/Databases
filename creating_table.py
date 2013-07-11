#03-07-2013
#creating a new table in an existing database

import sqlite3

def create_table(db_name,sql):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()


if __name__ == "__main__":
    db_name = "coffee_shop.db"
    sql = """create table Product
            (ProductID integer,
            Name text,
            Price real,
            primary key(ProductID))"""
    create_table(db_name, sql)

