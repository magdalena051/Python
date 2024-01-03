# if statement, if-elif(-else) blocks
# important: if only one of a number of conditions needs to be fulfilled, 
# use if-elif(-else) block.
# if multiple conditions can be true independently of each other, 
# use a series of if's


# ex 5-3

alien_color1 = "yellow" 
alien_color2 = "green" 
alien_color3 = "red" 

if alien_color1 == "green":
    print("You shot down the green alien. You get 5 points!")

if alien_color2 == "green":
    print("You shot down the green alien. You get 5 points!")
print("\n")


# ex 5-4

# if-block is not carried out, else block is carried out
if alien_color1 == "green":
    print("You shot down the green alien. You get 5 points!")
else: 
    print("You shot down a non-green alien. You get 10 points!")

# if-block is carried out
if alien_color2 == "green":
    print("You shot down the green alien. You get 5 points!")
else: 
    print("You shot down a non-green alien. You get 10 points!")
print("\n")


# ex 5-5

# if-block is carried out
if alien_color2 == "green":
    print("You shot down the green alien. You get 5 points!")
elif alien_color2 == "yellow":
    print("You shot down the yellow alien. You get 10 points!")
else:
    print("You shot down the red alien. You get 15 points!")

# elif-block is carried out
if alien_color1 == "green":
    print("You shot down the green alien. You get 5 points!")
elif alien_color1 == "yellow":
    print("You shot down the yellow alien. You get 10 points!")
else:
    print("You shot down the red alien. You get 15 points!")

# else-block is carried out
if alien_color3 == "green":
    print("You shot down the green alien. You get 5 points!")
elif alien_color3 == "yellow":
    print("You shot down the yellow alien. You get 10 points!")
else:
    print("You shot down the red alien. You get 15 points!")
print("\n")


# ex 5-6

age = 13
if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a child.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
elif age >= 65:
    print("The person is a senior.")
print("\n")


# ex 5-7

favorite_fruits = ["kakis", "bananas", "cherries"]

if "apples" in favorite_fruits:
    print("You like apples!")

if "bananas" in favorite_fruits:
    print("You like bananas!")

if "kakis" in favorite_fruits:
    print("You like kakis!")

if "tomatoes" in favorite_fruits:
    print("You like tomatoes!")

if "cherries" in favorite_fruits:
    print("You like cherries!")
    

    
    