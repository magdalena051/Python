
# ex 8-12 
# parameter with * takes an arbitrary number of arguments for that parameter 
# and stores the arguments in a tuple
def sandwiches(*toppings):
    print("\nYou have requested a sandwich with the following toppings: ")
    for topping in toppings:
        print("\t" + topping)
        
sandwiches("bacon", "lettuce", "tomato")
sandwiches("peanut butter", "jelly")
sandwiches("butter")
print()



# ex 8-13
# pass arbitrary number of keyword arguments via a dictionary.
# parameter with ** takes key value pairs and creates a dictionary of the same name
# (the name of the parameter) and the entries in the dictionary are the key-value 
# pairs that are passed in the function call.
# within the function, can treat the ** parameter as an ordinary dictionary.

def create_dictionary(**dictionary):
    return dictionary

dictionary = create_dictionary(key1="some value", key2="another value")
print(dictionary)

# function with positional parameters and arbitrary number of keyword parameters
def build_profile(first, last, **extra_info):
    # profile = {}
    # profile['first_name'] = first
    # profile['last_name'] = last
    profile = {
        'first_name' : first,
        'last_name' : last
        }
    for key, value in extra_info.items():
        profile[key] = value
    return profile

user_profile = build_profile("Maxi", "Muster", age="25", country="germany", \
                             fav_language="python")

print()
print(user_profile)





