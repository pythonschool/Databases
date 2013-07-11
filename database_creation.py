def create_customer(db,cursor):
    sql = """create table Customer (
             CustomerID integer,
             FirstName text,
             LastName text,
             Street text,
             Town text,
             PostCode text,
             TelephoneNumber text,
             primary key (CustomerID))"""

    cursor.execute(sql)
    db.commit()

def create_product_type(db,cursor):
    sql = """create table ProductType (
             ProductTypeID integer,
             Description text,
             primary key (ProductTypeID))"""
    
    cursor.execute(sql)
    db.commit()

def create_product(db,cursor):
    sql = """create table Product (
             ProductID integer,
             Name text,
             Price real,
             ProductTypeID integer,
             primary key (ProductID),
             foreign key (ProductTypeID) references ProductType(ProductTypeID)
             ON UPDATE CASCADE ON DELETE Restrict)"""
    
    cursor.execute(sql)
    db.commit()

def create_customer_order(db,cursor):
    sql = """create table CustomerOrder (
             OrderID integer,
             Date text,
             Time text,
             CustomerID integer,
             primary key (OrderID),
             foreign key (CustomerID) references Customer(CustomerID)
             ON UPDATE CASCADE ON DELETE Restrict)"""
    
    cursor.execute(sql)
    db.commit()

def create_order_items(db,cursor):
    sql = """create table OrderItem (
             OrderItemID integer,
             OrderID integer,
             ProductID integer,
             primary key (OrderItemID),
             foreign key (OrderID) references CustomerOrder(OrderID)
             ON UPDATE CASCADE ON DELETE Restrict,
             foreign key (ProductID) references Product(ProductID)
             ON UPDATE CASCADE ON DELETE Restrict)"""
    
    cursor.execute(sql)
    db.commit()


if __name__ == "__main__":

    import sqlite3

    db = sqlite3.connect("coffeeshop.db")
    cursor = db.cursor()
    create_customer(db,cursor)
    create_product_type(db,cursor)
    create_product(db,cursor)
    create_customer_order(db,cursor)
    create_order_items(db,cursor)
