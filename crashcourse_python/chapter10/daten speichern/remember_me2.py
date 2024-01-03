# Section saving and reading user generated data
# In this program, greet a user if they have already executed the program before, 
# and if they are new, store their name to a json file to greet them with next time

import json 

filename = "username2.json"

try:
    # open the file and save the name stored in the file to a variable
    with open(filename, 'r') as file_obj:
        username = json.load(file_obj)

except FileNotFoundError:
    # If the file does not exist (if the program hasn't been executed already 
    # and the file thereby created), ask the user for their name and save it 
    # to a json file
    username = input("What is your name? ")
    with open(filename, "w") as file_obj:
        json.dump(username, file_obj)
    print("Saved your name to a json file. We'll remember you when you come back, "
          + username + "!")

else:
    # Recall, this stuff is to be executed only if the stuff in the else block worked
    print("Welcome back, " + username + "!")
    