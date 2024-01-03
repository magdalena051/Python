# ex 7-7
# Varianten des programms "eintrittskarten": Abbruch der while Schleife über 
# Flag-Variable und über break-Anweisung
# Comment/ uncomment the program to be not run/ run

print("Welcome to the amusement park. ")
print("Enter your visitors' ages and I will tell you the price of their ticket.")
print("Enter 'quit' at any time to end.\n")
prompt = "Enter a visitor's age, 0-100: "
active = True


## Abbruch mittels Flag-Variable "active"
# while active:
#     age = input(prompt)
#     if age == "quit":
#         print("   Ending the program.")
#         active = False
#     elif 0 <= int(age) < 3:
#         print("   This visitor can enter for free.")
#     elif 3 <= int(age) <= 12:
#         print("   This visitor's ticket costs 12$.")
#     elif 12 < int(age) <= 100:
#         print("   This visitor's ticket costs 15$.")
#     else:
#         print("   Please enter a valid number: ")


# Abbruch mittels break-Anweisung
while True:
    age = input(prompt)
    if age == "quit":
        print("   Ending the program.")
        break
    elif 0 <= int(age) < 3:
        print("   This visitor can enter for free.")
    elif 3 <= int(age) <= 12:
        print("   This visitor's ticket costs 12$.")
    elif 12 < int(age) <= 100:
        print("   This visitor's ticket costs 15$.")
    else:
        print("   Please enter a valid number: ")







