# Chapter 9: classes
# classes contain functions called methods 
# class must always contain the __init__ method
# __init__ must take the parameter self



# ex 9-1
#
# define a class containing attributes and methods 
# note: don't forget self!
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print("Welcome to " + self.restaurant_name + " restaurant. We serve "
              + self.cuisine_type + " cuisine.")
    
    def open_restaurant(self):
        print(self.restaurant_name + " is open! Please come in.")
        
# create an instance of the class restaurant
restaurant = Restaurant("Anamit", "Vietnamese")

# print the attributes
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
print()
# call the methods
restaurant.describe_restaurant()
restaurant.open_restaurant()
print()



# 9-2 create several instances of the same class

restaurant1 = Restaurant("Mrs Zhao's Kitchen", "Chinese")
restaurant2 = Restaurant("Watzke", "German")
restaurant3 = Restaurant("Gianhis Fried Chicken", "Korean")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()



# 9-3
# same as 9-1 and 9-2: create a class with some attributes and methods, 
# create several instances of the class and call the methods for each instance

class User():
    def __init__(self, first_name, last_name, username, age):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age = age
        
    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name + "'s user details: \
              \n\tUsername: " + self.username + "\n\tAge: " + str(self.age))
            
    def greet_user(self):
        print("\nHello " + self.first_name + " " + self.last_name + "! "  
              + self.username + " is a nice username.")

user1 = User("Max", "Muster", "ok_computer", 28)
user2 = User("Jack", "Jones", "Beanstalk", 22)
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()


















