# ex 9-6
# create a class that inherits from another class

# parent class Restaurant
# parent class must be a part of the current file 
# (instead of copying the code, use import -> this comes later)
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print("Welcome to " + self.restaurant_name + " restaurant. We serve "
              + self.cuisine_type + " cuisine.")
    
    def open_restaurant(self):
        print(self.restaurant_name + " is open! Please come in.")
        

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        # initialize attributes of the parent class 
        # initialize attributes specific to an ice cream stand
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
        
    def set_flavors(self, flavors_list):
        self.flavors.extend(flavors_list)
    
    def get_flavors(self):
        print("\n" + self.restaurant_name + " offers the following flavors of ice cream:")
        for flavor in self.flavors:
            print("\t" + flavor.title())
            

my_icecreamstand = IceCreamStand("Ciao", "ice cream")
my_icecreamstand.set_flavors(["chocolate", "vanilla", "strawberry"])
my_icecreamstand.open_restaurant()
my_icecreamstand.get_flavors()
my_icecreamstand.set_flavors(["pistachio"])
my_icecreamstand.get_flavors()
