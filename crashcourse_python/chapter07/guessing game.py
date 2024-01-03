import random

num = random.randint(1,10)
guess = 0
active = True

print("I have a number between 1-10. Try to guess it.")
print("(Psst, the number is " + str(num) + ")")
guess = input("\nEnter your guess: ")

while active:
    if num == guess:
        print("\nYour guess is correct!")
        active = False
    else:
        guess = int(input("\nYour guess is not correct. Try again: "))
        