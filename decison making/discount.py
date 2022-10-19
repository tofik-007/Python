# A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.
Quantity = int(input("enetr the quantity of purchased item :"))
cost = Quantity * 100
discount = cost / 10
total_cost = cost - discount
if cost > 1000:
    print("you will get discount of ", discount)
    print("u have to pay ", total_cost ,"now")
else:
    print("u have to pay ", cost)
    
