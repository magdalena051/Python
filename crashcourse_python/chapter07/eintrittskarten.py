# ex 7-6

print("Welcome to the amusement park. ")
print("Enter your visitors' ages and I will tell you the price of their ticket.")
print("Enter 'quit' at any time to end.\n")
prompt = "Enter a visitor's age, 0-100: "
age = input(prompt)  


while age != "quit":
    if 0 <= int(age) < 3:
        print("   This visitor can enter for free.")
    elif 3 <= int(age) <= 12:
        print("   This visitor's ticket costs 12$.")
    elif 12 < int(age) <= 100:
        print("   This visitor's ticket costs 15$.")
    else:
        print("   Please enter a valid number: ")
    age = input(prompt)


print("   Ending the program.")