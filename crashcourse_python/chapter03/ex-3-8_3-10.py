
# =============================================================================
# Page 52
# cars = ["bmw", "audi", "toyota", "subaru"]
# sorted(cars, reverse=True)  # list sorted temporarily in reverse (nothing is done with it here)
# print(cars)                 # list is still unsorted
# cars.sort(reverse=True)     # list sorted permanently in reverse
# print(cars)                 # permanently reverse sorted list
# 
# =============================================================================



# ex 3-8

places = ["Denmark", "Canary Islands", "Egypt", "Australia", "Botswana"]

print("Favorite places, unsorted: ", end=(" ")) 
print(places)
print("Favorite places, temporarily sorted: ", end=(" "))
print(sorted(places))
print("Favorite places is still unsorted: ", end=(" "))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)