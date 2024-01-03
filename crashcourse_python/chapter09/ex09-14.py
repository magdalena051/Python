# ex 9-13
# skipped, since dictionaries are ordered from Python 3.7 upwards



# ex 9-14 
# create a class to simulate an n-sided dice, store number of sides as an attribute
# roll a 6-, 10-, and 20-sided dice 10 times each
from random import randint


class Die():
    """ A class to simulate dice """
    def __init__(self, sides=6):
        self.sides = sides
        
    def roll_die(self):
        x = randint(1, self.sides)
        return x

    def show_die_rolls(self, number):
        print("\nRolling a " + str(self.sides) + "-sided dice " + str(number) \
              + " times.")
        for i in range(0, number):
            print("\t" + str(self.roll_die()))


number_rolls = 10

die1 = Die(6)
die2 = Die(10)
die3 = Die(20)

die1.show_die_rolls(number_rolls)
die2.show_die_rolls(number_rolls)
die3.show_die_rolls(number_rolls)