# ex 9-4
# change a class attribute in three ways: 
# 1. edit the attribute directly, 
# 2. change the attribute value via a method, 
# 3. or increment the attribute value via a method (update the current 
#    attribute value by an increment amount)

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 # default value for the attribute 
                               # attributes of a class always need an initial value
        
    def describe_restaurant(self):
        print("Welcome to " + self.restaurant_name + " restaurant. We serve "
              + self.cuisine_type + " cuisine.")
    
    def open_restaurant(self):
        print(self.restaurant_name + " is open! Here is our menu.")
        
    def set_number_served(self, guests):
        self.number_served = guests
        
    def increment_number_served(self, new_guests):
        self.number_served += new_guests
    
    def get_number_served(self):
        print(self.restaurant_name + " has served " + str(self.number_served) + " guests today.")
        
    
restaurant = Restaurant("Anamit", "Vietnamese")
# way 1.
restaurant.number_served = 4
restaurant.get_number_served()
# way 2.
restaurant.set_number_served(7)
restaurant.get_number_served()
# way 3.
restaurant.increment_number_served(3)
restaurant.get_number_served()

