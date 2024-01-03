# Exercise 10-7
# Ask user for numbers until they quit. Add entered numbers together.
# If user enters faulty input, can still continue to enter input

print("Here is a program to add integers together. Enter 'q' at any point to quit.\n") 

numlist = []

while True:
    try:
        num = input("Enter an integer number: ")
        if num == "q":
            break
        numlist.append(int(num)) # append to list as long as it's an integer 
            
    except ValueError:
        print("\nThe last input is invalid. Please enter only integers!\n")

sum = 0
for number in numlist:
    sum += number
print("\nThe sum is: " + str(sum))


