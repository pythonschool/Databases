from controller_class import *

class CustomerController(CoffeeShopController):

    """creates a controller to add/delete/amend customer records in the
       coffee shop database"""

    def __init__(self):
        super().__init__()

    def add_customer(self,fn,ln,sa,t,pc,tn):
        sql = """insert into Customer
                 (FirstName,LastName,Street,Town,PostCode,TelephoneNumber)
                 values
                 (?,?,?,?,?,?)"""
        self.query(sql,(fn,ln,sa,t,pc,tn))
        
    def delete_customer(self,customer_id):
        sql = """delete from Customer
                 where CustomerID = ?"""
        self.query(sql,(customer_id,))
        
    def customer_details(self,customer_id=None,first_name=None,last_name=None):
        sql = None
        if customer_id != None:
            sql = "select * from Customer where CustomerID = ?"
            data = (customer_id,)
        elif first_name != None and last_name != None:
            sql = "select * from Customer where FirstName = ? and LastName = ?"
            data = (first_name,last_name)
        elif first_name != None:
            sql = "select * from Customer where FirstName = ?"
            data = (first_name,)
        elif last_name != None:
            sql = "select * from Customer where LastName = ?"
            data = (last_name,)
        if sql != None:
            return self.select_query(sql,data)
        else:
            return None
        
    def amend_customer(self,customer_id,first_name=None,last_name=None,street_address=None,town=None,post_code=None,telephone_number=None):
        updates = []
        data = []
        if first_name != None:
            updates.append(("FirstName",first_name))
        if last_name != None:
            updates.append(("LastName",last_name))
        if street_address != None:
            updates.append(("Street",street_address))
        if town != None:
            updates.append(("Town",town))
        if post_code != None:
            updates.append(("PostCode",post_code))
        if telephone_number != None:
            updates.append(("TelephoneNumber",telephone_number))
        
        sql = "update Customer set "
        for item in updates:
            sql += "{0}=?, ".format(item[0])
            data.append(item[1])
        
        #remove last ', '
        sql = sql[:-2]
        sql += " where CustomerID=?"
        data.append(customer_id)
        self.query(sql,data)

    def customer_headings(self):
        sql = "PRAGMA table_info(Customer)"
        return self.select_query(sql)
        
        
    
        
