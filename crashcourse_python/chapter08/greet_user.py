# two versions of a simple function

# 1.
# function is called as soon as program is run and input is taken within the function
def greet_user():
    n = input("What is your name? ")
    print("Hello, " + n + "!")
    
greet_user()


# 2.
# input is first taken and function is called only after user has entered input, 
# taking the inputted information as a variable
def greet_user(n):
    print("Hello, " + n + "!")
    
name = input("What is your name? ")
greet_user(name)