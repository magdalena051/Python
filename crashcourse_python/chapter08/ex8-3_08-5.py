
# ex 8-3 
# calling a function using position dependent arguments, and using keyword arguments

def make_shirt(size, text):
    print("\nYour t-shirt order: \n\tSize: " + size + "\n\tText: " + text)
    
# position dependent arguments: position must be the same as in the function definition
make_shirt("S", "Cat person")
make_shirt("Cat person", "S")

# keyword arguments: position doesn't matter, but takes more typing
make_shirt(size="S", text="Cat person")
make_shirt(text="Cat person", size="S")
print()



# ex 8-4 
# function with default arguments, changing none, some or all of the default arguments

def make_shirt2(size="L", text="I love Python"):
    print("\nYour t-shirt order: \n\tSize: " + size + "\n\tText: " + text)
    
# t-shirt with standard size and standard text
make_shirt2()

# t-shirt with different size and standard text
make_shirt2(size="M")

# t-shirt with standard size and different text
make_shirt2(text="The GOAT")

# t-shirt with different size  and different text
make_shirt2(size="S", text="The GOAT")
print()



# ex 8-5
# function with one default arg, and one non default arg

def describe_city(city, country="Germany"):
    print("The city " + city + " is in " + country + ".")

# city happens to match the default country
describe_city("Berlin")

# city is not in default country -> wrong output
describe_city("Washington DC")

# changing the default value for country to match the city
describe_city("Washington DC", "America")






