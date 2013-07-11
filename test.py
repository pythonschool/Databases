from customer_controller import *
from product_controller import *
from order_controller import *

test = CustomerController()
#print(test.customer_details(first_name="Emma"))
#print(test.customer_details(last_name="Bain"))
test.add_customer("Adam","McNicol","1 Python Street","Cambridge","CB3 2YU","01223 467893")
test.amend_customer("16",first_name="Bob")
print(test.customer_headings())

test = OrderController()
print(test.new_empty_order("1"))
