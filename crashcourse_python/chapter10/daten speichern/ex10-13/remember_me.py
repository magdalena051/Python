# an extension of the program remember_me.py (version on page 239)
# Ask for user's name and store the name. Next time the program is run, ask 
# user if their name is the previously stored name. If yes, greet the user. 
# If no, ask for name again and overwrite stored name with new name.

import json 

def get_stored_username():
    """Get stored username if available."""
    filename = "username.json"
    try:
        with open(filename, 'r') as file_obj:
            username = json.load(file_obj)
    except FileNotFoundError:
        return None
    else:
        return username     # only return username if code in try block worked
                            # (if no filenotfound error occured)

def get_new_username():
    """Prompt for a new username"""
    username = input("What is your name? ")
    filename = "username.json"
    with open(filename, "w") as file_obj:
        json.dump(username, file_obj)
    return username


def greet_user():
    username = get_stored_username()
    if username:
        response = input("Is your name " + username + "? (y/n) ")
        if response == "y":
            print("Hello, " + username + "! I remember you.")
        elif response == "n":
            username = get_new_username()
            print("I'll remember you when you come back, " + username + "!")
    else:
        username = get_new_username()
        print("I'll remember you when you come back, " + username + "!")

greet_user()


# delete the file "username.json" generated by the program after calling