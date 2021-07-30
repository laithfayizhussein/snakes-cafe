print ( """ **************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
""")

the_menu = ['wings', 'cookies', 'spring rolls', 'salmon', 'steak', 'meat tornado',
            'a literal garden', 'ice Cream', 'cake', 'pie', 'coffee', 'tea', 'unicorn tears']

user_order = [] 

order_name = []


def make_order ():

     order = input ('>')
     if order.lower() in the_menu:
         user_order.append(order)
         if order not in order_name :
             order_name.append(order)
         print (f"** u have {user_order.count(order)} of {order} add to your meal **" )

         make_order()

     elif order.lower() == 'quit' :
         print ('your order is ')
         for i in order_name :
             print (f"u have {user_order.count(i)} of {i}")
     elif order.lower () not in the_menu :
         print (f"where are sorry the item not avalible yet")
         make_order()
make_order()

