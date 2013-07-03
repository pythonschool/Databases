#03-07-2013
#creating a new table in an existing database

import sqlite3

def create_table(db_name,table_name,sql):
    with sqlite3.connect(db_name) as db:
        print(table_name)
        cursor = db.cursor()
        cursor.execute("select name from sqlite_master where name=?",(table_name,))
        result = cursor.fetchall()
        keep_table = True
        if len(result) == 1:
            response = input("The table {0} already exists, do you wish to recreate it? (y/n): ".format(table_name))
            if response == "y":
                keep_table = False
                print("The {0} table will be recreated - all existing data will be lost".format(table_name))
                cursor.execute("drop table if exists {0}".format(table_name))
                db.commit()
            else:
                print("The existing animal table was kept")
        else:
            keep_table = False
        if not keep_table:
            cursor.execute(sql)
            db.commit()

if __name__ == "__main__":
    db_name = "coffee_shop.db"
    sql = """create table product
            (product_id integer,
            name text,
            price real,
            primary key(product_id))"""
    create_table(db_name, "product", sql)

