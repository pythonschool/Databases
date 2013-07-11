#03-07-2013
#inserting data into tables with reference to other tables

from database_functions import query

def insert_product_data(records):
    sql = "insert into Product (Name,Price,ProductTypeID) values (?,?,?)"
    for record in records:
        query(sql, record)

def insert_product_type_data(records):
    sql = "insert into ProductType(Description) values (?)"
    for record in records:
        query(sql, record)

if __name__ == "__main__":
    products = [("Americano",2.0,1),("Mocha",3.5,1),("Green Tea with Lemon",1.25,2)]
    insert_product_data(products)
    product_types = [("Coffee",),("Tea",),("Cold Drink",)]
    insert_product_type_data(product_types)