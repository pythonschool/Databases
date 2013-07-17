import sqlite3

class CoffeeShopController:

    def __init__(self):
        self.dbtext = "coffeeshop.db"
        
    def query(self,sql,data):
        with sqlite3.connect(self.dbtext) as db:
            cursor = db.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute(sql,data)
            db.commit()

    def select_query(self,sql,data=None):
        with sqlite3.connect(self.dbtext) as db:
            cursor = db.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            if data:
                cursor.execute(sql,data)
            else:
                cursor.execute(sql)
            results = cursor.fetchall()
        return results

        
