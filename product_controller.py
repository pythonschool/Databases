from controller_class import *

class ProductController(CoffeeShopController):
    """creates a controller to add/delete/amend product records in the
       coffee shop database"""

    def __init__(self):
        super().__init__()

    def add_product(self,name,price,product_type):
        sql = """insert into Product (Name, ProductTypeID, Price)
                 values (?,?,?)"""
        self.query(sql,(name,product_type,price))

    def delete_product(self,product_id):
        sql = "delete from Product where ProductID = ?"
        self.query(sql,(product_id,))

    def product_details(self,product_id=None,name=None):
        sql = None
        data = []
        if product_id != None:
            sql = "select * from Product where ProductID = ?"
            data = (product_id,)
        elif name != None:
            sql = "select * from Product where Name = ?"
            data = (name,)
        else:
            sql = "select * from Product"
        return self.select_query(sql,data)

    def amend_product(self,product_id,name=None,product_type_id=None,price=None):
        updates = {}
        data = []
        if name != None:
            updates["Name"] = name
        if product_type_id != None:
            updates["ProductTypeID"] = product_type_id
        if price != None:
            updates["Price"] = price

        sql = "update Product set "
        for key, value in updates.items():
            sql += "{0}=?, ".format(key)
            data.append(value)

        sql = sql[:-2]
        sql += " where ProductID = ?"
        data.append(product_id)

        self.query(sql,data)

    def product_headings(self):
        sql = "PRAGMA table_info(Product)"
        return self.select_query(sql)

    def add_product_type(self,name):
        sql = "insert into ProductType (Description) values (?)"
        self.query(sql,(name,))

    def delete_product_type(self,product_type_id):
        sql = "delete from ProductType where ProductTypeID = ?"
        self.query(sql,(product_type_id,))

    def amend_product_type(self,product_type_id,name):
        sql = "update ProductType set Name = ? where ProductTypeID = ?"
        self.query(sql,(name,product_type_id))

    def product_type_details(self,product_type_id=None,name=None):
        if product_type_id != None:
            sql = "select * from ProductType where ProductTypeID = ?"
            data = (product_type_id,)
        elif name != None:
            sql = "select * from ProductType where Name = ?"
            data = (name,)
        return self.select_query(sql,data)

    def product_type_headings(self):
        sql = "PRAGMA table_info(ProductType)"
        return self.select_query(sql)