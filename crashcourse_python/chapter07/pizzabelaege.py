# ex 7-4
# "Pizzabeläge"

print("Please enter toppings you would like to have on your pizza.")
print("Enter quit to end.")

topping = ""
toppings = []

while topping != "quit":
    topping = input("\nEnter a topping: ")
    if topping != "quit":
        print("Adding " + topping + " to your pizza.")
        toppings.append(topping)
  
print("\nYour pizza with the following toppings")
for item in toppings:
    print("   " + item)
print("is complete. Enjoy!")
