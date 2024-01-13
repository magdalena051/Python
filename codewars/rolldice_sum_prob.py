# Exercise source: 
# https://www.codewars.com/kata/56f78a42f749ba513b00037f/python
# https://www.codewars.com/kata/56f852635d7c12fb610013d7
# We have a certain number of dice each with a certain number of sides. 
# We roll these dice and take the sum of the resulting face values.
# This program calculates a distribution for this procedure. 
# We display the distribution: for each possible sum, how many different rolls 
# yield that sum (number of hits).


import math as m
import matplotlib.pyplot as plt 


# Returns the number of possible dice rolls using dice_amt dice which sum to the sum sum_.
# Dice have six sides by default.
# Formula for how many ways there are to roll a total of sum_ using dice_amt dice taken from
# https://www.quora.com/Is-there-a-formula-to-calculate-the-probability-of-the-sum-of-x-dice-being-than-y    
def rolldice_sum_hitcount(sum_, dice_amt, sides=6):
    if sum_<dice_amt or sum_>(dice_amt*sides):
        hitcount = 0
    else:
        sum_end = m.floor((sum_-dice_amt)/sides)
        res = 0
        for i in range(0, sum_end+1):
            res += (-1)**i * m.comb(dice_amt, i) * m.comb(sum_-sides*i-1, dice_amt-1)
            # comb() : binomial coefficient
        hitcount = res
    return hitcount 


# Returns probability of rolling the sum sum_ using dice_amt dice
# sides**dice_amt is the total number of possible dice roll combinations
def rolldice_sum_prob(sum_, dice_amt, sides=6):   
    hitcount = rolldice_sum_hitcount(sum_, dice_amt, sides)
    prob = hitcount / (sides**dice_amt)
    return prob             


# For given dice amount with given number of sides, returns a register of hits
# for each possible sum value
def reg_sum_hits(dice_amt, sides=6):
    res = []
    for sum_ in range (dice_amt, dice_amt*sides+1):
        hits = rolldice_sum_hitcount(sum_, dice_amt, sides)
        res.append([sum_, hits])
    return res
#
# Example:
# reg_sum_hits(3,4) returns
# [[3, 1], [4, 3], [5, 6], [6, 10], [7, 12], [8, 12], [9, 10], [10, 6], [11, 3], [12, 1]]
# Throwing three 4-sided dice, there is one possibility where the dice sum to 3,
# three possibilities where the dice sum to four, six possibilities where the dice sum to 5, 
# ... one possibility where the dice sum to 12.  


def plot_results(dice_amt, sides=6):
    fig, ax = plt.subplots()
    # get data, dice sums are x-values, no. of hits are y-values
    data = reg_sum_hits(dice_amt, sides)
    x = []
    y = []
    for i in data:
        x.append(i[0])
        y.append(i[1])    
    ax.bar(x, y) 
    ax.set_xlabel('Sum value')
    ax.set_ylabel('Number of hits')
    plt.show()
    

print(reg_sum_hits(5,4))
plot_results(5,4)        



