from controller_class import *
import datetime

class OrderController(CoffeeShopController):
    """creates a controller to add/delete/amend product orders in the
       coffee shop database"""

    def __init__(self):
        super().__init__()

    def new_empty_order(self,customer_id):
        sql = "insert into CustomerOrder (Date,Time,CustomerID) values (?,?,?)"
        date = datetime.datetime.now()
        time = datetime.datetime.now()
        self.query(sql,(date,time, customer_id))
        sql = "select OrderID from CustomerOrder where CustomerID = ? and Date = ?"
        return self.select_query(sql,(customer_id,date))

    def add_order_items(self,order_id,items):
        sql = "insert into OrderItem (OrderID,ProductID) values (?,?)"
        for item in items:
            self.query(sql,(order_id,item))

    def new_order_with_items(self,customer_id,items):
        order_id = self.new_empty_order(customer_id)
        self.add_order_items(order_id, items)

    def delete_order(self,customer_id,date):
        sql = "delete from CustomerOrder where CustomerID = ? and Date = ?"
        self.query(sql,(customer_id,date))

    def delete_order_items(self,order_id,items):
        sql = "delete from OrderItem where OrderID = ? and ProductID = ?"
        for item in items:
            self.query(sql,(order_id,item))

    def order_details(self,customer_id,date):
        sql = """select CustomerOrder.Date, CustomerOrder.OrderID, product.ProductID
                 from CustomerOrder, OrderItem, Product
                 where CustomerOrder.CustomerID = ? 
                 and CustomerOrder.Date = ? 
                 and OrderItem.OrderID = CustomerOrder.OrderID 
                 and Product.ProductID = OrderItem.ProductID"""
        return self.select_query(sql,(customer_id,date))

    def customer_orders(self,customer_id):
        sql = "select * from CustomerOrder where CustomerID=?"
        return self.select_query(sql,(customer_id,))

    def orders_on_date(self,date):
        sql = "select * from CustomerOrder where Date like ?%"
        return self.select_query(sql,(date,))

    

