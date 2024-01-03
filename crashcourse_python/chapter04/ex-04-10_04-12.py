# making and using slices (sublists of lists)


# list we'll be using in these exercises
pizzas = ["Salami", "Tonne", "Hawaii", "Funghi", "Tex Mex", "Diavola"]

# ex 4-10
# print first three, middle three, and last three items of a list
print("The first three items in the list are: ")
print(pizzas[:3])
print("\nThree items from the middle of the list are:")
print(pizzas[2:5])
print("\nThe last three items in the list are:")
print(pizzas[-3:])


# ex 4-11
# make a copy of the first list,
# make changes to the list copy and the first list 
# thereby showing that the two lists are different
friend_pizzas = pizzas[:]
pizzas.append("Margherita")
friend_pizzas.append("Prosciutto")
print("\nMy favorite pizzas are: ")
for pizza in pizzas: 
    print(pizza)
print("\nMy friend's favorite pizzas are: ")
for pizza in friend_pizzas: 
    print(pizza)