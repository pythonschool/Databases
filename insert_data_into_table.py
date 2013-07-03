#03-07-2013
#inserting data into an existing table

import sqlite3

def insert_data(values):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        sql = "insert into product (name,price) values(?,?)"
        cursor.execute(sql,values)
        db.commit()

if __name__ == "__main__":
    product = ("Espresso",1.5)
    insert_data(product)