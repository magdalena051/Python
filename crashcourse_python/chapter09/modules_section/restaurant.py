# ex 9-10

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print("Welcome to " + self.restaurant_name + " restaurant. We serve "
              + self.cuisine_type + " cuisine.")
    
    def open_restaurant(self):
        print(self.restaurant_name + " is open! Please come in.")
        
