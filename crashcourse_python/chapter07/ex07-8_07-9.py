def listtostring(a_list):
    string = ""
    for item in a_list[0:-1]:
        string += item + ", "
    string += a_list[-1]
    return string

# ex 7-8 

bagel_orders = ["cream cheese", "lox", "BLT", "pastrami"]
completed_bagels = []

while bagel_orders:  # while loop continues as long as list is not empty
    current_order = bagel_orders.pop()
    print("Preparing your " + current_order + " bagel...")
    completed_bagels.append(current_order)
    
print("The following bagels have been prepared: ")
bagels = listtostring(completed_bagels)
print("    " + bagels)
print("")



# ex 7-9


bagel_orders = ["cream cheese", "lox", "pastrami", "BLT", "pastrami", "pastrami"]
runout_item = "pastrami"
print("The following bagel orders have been placed: ")
orders_string = listtostring(bagel_orders)
print("    " + orders_string)
print("Sorry, we've run out of " + runout_item + ".")
while runout_item in bagel_orders:
    bagel_orders.remove(runout_item)
print("We can only complete the following orders:")
orders_string = listtostring(bagel_orders)
print("    " + orders_string)

    
    