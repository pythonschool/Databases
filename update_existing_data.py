#03-07-2013
#update existing data

import sqlite3

def update_product(data):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        sql = "update product set name=?, price=? where product_id=?"
        cursor.execute(sql,data)
        db.commit()

if __name__ == "__main__":
    data = ("Latte",2.45,1)
    update_product(data)