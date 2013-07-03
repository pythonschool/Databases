#03-07-2013
#product menu

import sqlite3

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
                print("The existing animal table was kept")
        else:
            keep_table = False
        if not keep_table:
            cursor.execute(sql)
            db.commit()

def query(sql,data):
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        cursor.execute(sql,data)
        db.commit()

def query_with_results(sql,data):
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        if data == None:
            cursor.execute(sql)
        else:
            cursor.execute(sql,data)
        results = cursor.fetchall()
        return results

def query_with_single_result(sql,data):
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        cursor.execute(sql,data)
        result = cursor.fetchone()
        return result

def delete_product(data):
    sql = "delete from product where name=?"
    query(sql,data)

def insert_data(values):
    sql = "insert into product (name,price) values(?,?)"
    query(sql,values)

def update_product(data):
    sql = "update product set name=?, price=? where product_id=?"
    query(sql,data)

def select_all_products():
    sql = "select * from product"
    return query_with_results(sql,None)

def select_product(id):
    sql = "select * from product where product_id=?"
    return query_with_single_result(sql,(id,))

def select_product_with_name(name):
    sql = "select * from product where name=?"
    return query_with_single_result(sql,(name,))

def display_menu():
    print("Product Table Menu")
    print()
    print("1. (Re)Create Product Table")
    print("2. Add new product")
    print("3. Edit existing product")
    print("4. Delete existing product")
    print("5. Search for products")
    print("0. Exit")
    print()

def get_menu_choice():
    accepted = False
    while not accepted:
        choice = int(input("Please select an option: "))
        if 0 <= choice <= 5:
            accepted = True
        else:
            print("Pleae enter a valid value")
    return choice

def display_select_results(results):
    if results[0] != None:
        print()
        print("{0:<15} {1:<15} {2:<15}".format("Product ID","Product Name", "Product Price"))
        for result in results:
            print("{0:<15} {1:<15} {2:<15}".format(result[0],result[1],result[2]))
        print()
    else:
        print("The query returned no results")


def main():
    finished = False
    while not finished:
        display_menu()
        choice = get_menu_choice()
        if choice == 1:
            sql = """create table product
            (product_id integer,
            name text,
            price real,
            primary key(product_id))"""
            create_table("product",sql)
        elif choice == 2:
            name = input("Please enter name of new product: ")
            price = float(input("Please enter the price of {0}: ".format(name)))
            insert_data((name,price))
        elif choice == 3:
            products = select_all_products()
            display_select_results(products)
            product_id = int(input("Please enter the id of the product to edit: "))
            name = input("Please enter new name for the product: ")
            price = float(input("Please enter the price of {0}: ".format(name)))
            update_product((name,price,product_id))
        elif choice == 4:
            products = select_all_products()
            display_select_results(products)
            product_id = int(input("Please enter the id of the product to delete: "))
            product = select_product(product_id)
            delete_product((product[1],))
        elif choice == 5:
            name = input("Please enter the name of the product to search for: ")
            product = select_product_with_name(name)
            display_select_results([product])
        elif choice == 0:
            finished = True


if __name__ == "__main__":
    DATABASE = "coffee_shop.db"
    main()


