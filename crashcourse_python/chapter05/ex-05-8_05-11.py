

# ex 5-8

usernames = ["unicorn", "machoman", "admin", "Bob", "Sally"]

for username in usernames:
    if username == "admin":
        print("Hello Admin, logging you in. You are special.")
    else:
        print("Hello " + username + ", logging you in.")
print("\n")



# ex 5-9

usernames2 = []

if usernames2:
    for username in usernames2:
        if username == "admin":
            print("Hello Admin, logging you in. You are special.")
        else:
            print("Hello " + username + ", logging you in.")
else:
    print("There are no users to log in!")
print("\n")



# ex 5-10

current_users = ["olaf", "klothilde", "waltraud", "siegfried", "heinz"]
new_users = ["Kevin", "WAltraud", "Heinz", "Herbert", "Irma"]
for user in new_users:
    if user.lower() in current_users:
        print("Sorry, the username " + user + " is already taken.")
    else: 
        print("Great name, " + user + "! Your name is not taken.")
print("\n")


# ex 5-11

digits = [x for x in range(1,10)]

for digit in digits:
    print("Ordinal of " + str(digit) + ": ", end=(""))
    if digit == 1:
        print(str(digit) + "st")
    elif digit == 2:
        print(str(digit) + "nd")
    elif digit == 3:
        print(str(digit) + "rd")
    else: 
        print(str(digit) + "th")
print("\n")


        
        


