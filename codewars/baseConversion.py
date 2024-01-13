# Convert a number from one base to another. The bases must be chosen between base 2-36.
# Input:  - number to be converted (string) in source base, 
#         - source base (integer between 2 and 36), 
#         - target base (integer between 2 and 36)
# Output: - number in target base
# Input is assumed to be correct; input number only contains characters from from the
# source base (e.g. when converting a binary number, the number only contains characters 0 or 1)
#
# General steps for converting a number between two bases:
# 1. 
# Convert from  source base to base 10 
# decimal representation = ∑(digit×base^(digit number))
# e.g. (534)_8 = (5 × 8^2) + (3 × 8^1) + (4 × 8^0) = (348)_10
#      (53B)_12 = (5 × 12^2) + (3 × 12^1) + (11 × 12^0) = (767)_10
#
# 2.
# Convert from decimal to destination base: divide the decimal with the base 
# until the quotient is 0 and calculate the remainder each time. The destination 
# base digits are the calculated remainders.
# Example:
# Decimal to base 12 calculation:
# Divide by the base to get the digits from the remainders:
# ________________________________________________
# Division	|Quotient  |Remainder (digit) |Digit #
# 767/12	|63	       |11	              |0
# 63/12	    |5	       |3	              |1
# 5/12	    |0	       |5	              |2
# = (53B)_12



############### generate dictionaries ###############
def strToDict(st):
    lst = list(st)
    dct = {}
    for index, element in enumerate(lst):
        dct[index] = element
    return dct

digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digitsDict = strToDict(digits)                 # {0:'0', 1:'1', ... 10:'A',..., 36:'Z'}
invDigitsDict = {v: k for k, v in digitsDict.items()}
#####################################################


# Return number num given in source base, in its base 10 representation
# num should be string 
# returns int
def sourceBaseToBase10(num, sb=10):
    # ingredients: 
    #       powers 0,... len(num)-1
    #       digits of num in decimal form
    dct = invDigitsDict
    res = 0
    base = sb
    exp = len(num)-1
    for digit in num:
        factor = dct[digit]
        res = res + int(factor) * base**exp
        #print(str(factor) + "*" + str(base) + "^" + str(exp) + "+" )
        exp = exp-1
    return res


# return the remainder of dividend/divisor
def divRemainder(dividend, divisor):
    remainder = dividend%divisor
    return remainder


# return the quotient of dividend/divisor (how many times divisor fits into 
# dividend without any remainder)
def divQuotient(dividend, divisor):
    remainder = dividend%divisor
    quotient = (dividend-remainder)/divisor
    return quotient


# return a string in reverse
def revString(st):
    res = st[::-1]
    return res

# Convert the number num (which is in base 10) to goal base gb and place each
# conversion step into an array, output the array
# (Example: see the decimal to base 12 example at the top of this file; the
# rows in the table correspond to rows of the output array here
def base10toGoalBaseSteps(num, gb):
    quotient = num
    step = ()
    steps = []
    if quotient == 0:
        return digitsDict[0]
    while quotient != 0:
        division = str(quotient) + "/" + str(gb)
        remainder = int(divRemainder(quotient, gb))
        quotient = int(divQuotient(quotient, gb))
        digit = digitsDict[remainder]
        step = (division, str(quotient), str(remainder), digit)
        steps.append(step)
    return steps


# Return the number num (which is in base 10) to goal base gb by reading the 
# digits from the last "column" of the array returned by the function above,
# then reverse the characters to get them in correct order
def base10toGoalBase(num, gb):
    steps = base10toGoalBaseSteps(num, gb)
    res = ""
    if num == 0: # special case 0
        return digitsDict[0]
    for step in steps:
        res = res + step[3]
    return revString(res)


# bring everything together
def convertBetwBases(num, b, g):
    num = str(num)
    # convert input num from base b1 to base 10
    numInb10 = sourceBaseToBase10(num, b)
    # convert num in base ten to base b2
    numInBaseg = base10toGoalBase(numInb10, g)
    return numInBaseg


# Examples

num1 = "101110111101"
b1 = 2 
g1 = 15

num2 = "Z" 
b2 = 36
g2 = 10

num3 = "ABCDEF"
b3 = 16
g3 = 10

num4 = "11259375"
b4 = 10
g4 = 16

num5 = "HELLO"
b5 = 25
g5 = 10

num6 = "0"
b6 = 2
g6 = 10


print(convertBetwBases(num1, b1, g1))
print(convertBetwBases(num2, b2, g2))
print(convertBetwBases(num3, b3, g3))
print(convertBetwBases(num4, b4, g4))
print(convertBetwBases(num5, b5, g5))
print(convertBetwBases(num6, b6, g6))

