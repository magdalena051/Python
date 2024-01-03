# Passing arguments to functions

def describe_pet1(pet_name, animal_type):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name + ".")
    

def describe_pet2(pet_name, animal_type="dog"):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name + ".")
    
    
# # leads to an error without even calling the function;
# # python doesn't let you place non-default arguments after default arguments
# def describe_pet3(animal_type="dog", pet_name):
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name + ".")
    

# position dependent variables
describe_pet1("Ollie", "cat")


# can switch the order in position-dependent function call if you explicitly 
# pass the variables to their parameters
describe_pet1(animal_type="cat", pet_name="Ollie")


# changing the value of the default argument
describe_pet2("Ollie", "cat")

# also here, can switch the order in function call if you explicitly pass the 
# variables to their parameters
describe_pet2(animal_type="cat", pet_name="Ollie")


# switching the order can lead to unwnated results
describe_pet2("cat", "Ollie")

# erroneous function
# describe_pet3("Ollie")