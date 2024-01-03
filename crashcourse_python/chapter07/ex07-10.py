
print("A poll for holiday destinations.")

responses = {} # empty dictionary

active = True

while active:
    name = input("\nWhat is your name? ")
    response = input("If you could go on holiday now, where would you go? ")
    responses[name] = response  # assign the value response to the key name
    
    repeat = input("Would you like to let another person respond? (yes/no) : ")
    if repeat == "no":
        active = False
        
print("\nPoll results:")
for name, place in responses.items():
    print(name + " would like to visit " + place + ".")
