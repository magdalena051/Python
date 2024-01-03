
# ex 5-1
# write a number of conditions that evaluate to true and false

number = 51

print("I guess the number is less than 100.")
print(number < 100)

print("\nI guess the number is less than 42.")
print(number < 42)

print("\nI guess the number is less than 75.")
print(number < 75)

print("\nI guess the number is greater than 50.")
print(number > 50)

print("\nI guess the number is greater than or equal 51.")
print(number >= 51)

print("\nI guess the number is greater than or equal 55.")
print(number >= 55)

print("\nI guess the number is equal to 51.")
print(number == 51)


# ex 5-2
# check for equality/ inequality of strings, also using lower()
# check numbers for greater than, less than
# use and, or conditions
# check if an element is in / not in a list
str1 = "Dog"
str2 = "Cat" 

print("\nIs the first word identical to 'cat'?")
print(str1 == "cat")
print("\nIs the second word identical to 'cat'?")
print(str2 == "cat")

print("\nDoes the first word spell 'cat'?")
print(str1.lower() == "cat")
print("\nDoes the second word spell 'cat'?")
print(str2.lower() == "cat")

num1 = 9 
num2 = 33

print("\nAre both numbers positive?")
print(num1 > 0 and num2 > 0)

print("\nAre both numbers greater than 10?")
print(num1 > 10 and num2 > 10)

print("\nIs one of the numbers greater than 10?")
print(num1 > 10 or num2 > 10)

print("\nIs one of the numbers less than 5?")
print(num1 < 5 or num2 < 5)



fruits = ["bananas", "apples", "strawberries", "tomatoes"]
print("\nAre tomatoes a fruit?")
print("tomatoes" in fruits)
print("\nAre cucumbers a fruit?")
if "cucumbers" not in fruits:
    print("Cucumbers are not in the fruits list. They might still be a fruit though.")
else:
    print("Cucumbers are in the fruits list. They are a fruit.")




