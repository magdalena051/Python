# Exercise 10-6
# Ask user for two numbers until they quit. Add the entered numbers together

print("Here is a program to add two integers together. Enter 'q' to quit.\n") 

while True:
    
    try:
        num1 = input("Enter an integer number: ")
        if num1 == "q":
            break
        num2 = input("Enter another integer number: ")
        if num2 == "q":
            break 
        sum = int(num1) + int(num2)
        
    except ValueError:
        print("Invalid input. Please enter only integers!\n")
    
    else:
        print("The sum is: " + str(sum) + "\n")

