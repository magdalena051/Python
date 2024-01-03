# ex 9-10
# try out the import statement:
# save Restaurant class in a separate module (saved it in restaurant.py), import 
# the Restaurant class, create an instance of Restaurant and use the class methods 

from restaurant import Restaurant

my_restaurant = Restaurant("Anamit", "Vietnamese")
my_restaurant.open_restaurant()
my_restaurant.describe_restaurant()