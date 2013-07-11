#03-07-2013
#adding relationships to tables
import sqlite3

def query(sql,data):
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        cursor.execute(sql,data)
        db.commit()

def create_table(table_name,sql):
    with sqlite3.connect(DATABASE) as db:
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
                print("The existing table was kept")
        else:
            keep_table = False
        if not keep_table:
            cursor.execute(sql)
            db.commit()

def create_product_type_table():
    sql = """create table ProductType(
            ProductTypeID integer,
            Description text,
            primary key(ProductTypeID))"""
    create_table("ProductType",sql)

def create_product_table():
    sql = """create table Product
            (ProductID integer,
            Name text,
            Price real,
            ProductTypeID integer,
            primary key(ProductID),
            foreign key(ProductTypeID) references ProductType(ProductTypeID))"""
    create_table("Product",sql)

if __name__ == "__main__":
    DATABASE = "coffee_shop.db"
    create_product_type_table()
    create_product_table()