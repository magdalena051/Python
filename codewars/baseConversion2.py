# Exercise source: https://www.codewars.com/kata/526a569ca578d7e6e300034e
#
# Similar to baseConversion.py, but here arbitrary bases beyond base 2-36 are possible. 
# Input:  - number to be converted (string containing only characters from source alphabet),
#         - source base (string containing the characters of the source base, each character
#           should be distinct and ordered from smallest to greatest value)
#         - target base (string containing the characters of the target base, each character
#           should be distinct and ordered from smallest to largest value))
# Output: - number in target base
#
# General steps for converting a number between two bases:
# 1. 
# Convert from  source base to base 10:
# decimal = ∑(digit×basedigit number)
# e.g. (534)_8 = (5 × 8^2) + (3 × 8^1) + (4 × 8^0) = (348)_10
#      (53B)_12 = (5 × 12^2) + (3 × 12^1) + (11 × 12^0) = (767)_10
#
# 2.
# Convert from decimal to destination base: divide the decimal with the base 
# until the quotient is 0 and calculate the remainder each time. The destination 
# base digits are the calculated remainders.
# Example:
# Convert 767 from base 10 to base 12.
# Divide by the base to get the digits from the remainders:
# _________________________________________________
# Division	|Quotient  |Remainder (digit) |Digit no.
# 767/12	|63	       |11	              |0
# 63/12	    |5	       |3	              |1
# 5/12	    |0	       |5	              |2
# = (53B)_12
###############################################################################


# Example bases
bin           = '01'
oct           = '01234567'
dec           = '0123456789'
hex           = '0123456789abcdef'
allow         = 'abcdefghijklmnopqrstuvwxyz'
allup         = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha         = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphanum      = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
decAlphaUp    = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
decAlphaLowUp = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
rev           = '9876543210'


# Generate dictionary
# Decimal numbers are keys, elements of the string st are values
# Characters of the string st represent digits of the base
# Characters of the string st should be ordered from smallest to largest value
def strToDict(st):
    lst = list(st)
    dct = {}
    for index, element in enumerate(lst):
        dct[index] = element
    return dct


# Generate dictionary 
# Elements of the string st are keys, decimal numbers are values 
def invStringToDict(st):
    dct = strToDict(st)
    invDct = {v: k for k, v in dct.items()}
    return invDct


# Return number num given in source base, in its base 10 representation
# num must be string 
def sourceBaseToBase10(num, sb=dec):
    # ingredients: 
    #       powers 0,... len(num)-1
    #       digits of num in decimal form
    dct = invStringToDict(sb)
    res = 0
    base = len(sb)
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


# return the quotient of dividend/divisor
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
# num is int (sourceBaseToBase10 returns int, check)
# gb is string, similar to sb
def base10toGoalBaseSteps(num, gb):
    dct = strToDict(gb)
    base = len(gb)
    quotient = num 
    step = ()
    steps = []
    if num == 0:
        return dct[0]
    while quotient != 0:
        division = str(quotient) + "/" + str(base)
        remainder = int(divRemainder(quotient, base))
        quotient = int(divQuotient(quotient, base))
        digit = dct[remainder]
        step = (division, str(quotient), str(remainder), digit)
        steps.append(step)
    return steps


# Return the number num (which is in base 10) to goal base gb by reading the 
# digits from the last "column" of the array returned by the function above,
# then reverse the characters to get them in correct order
def base10toGoalBase(num, gb):
    if num == 0:
        return base10toGoalBaseSteps(num, gb)
    else:
        steps = base10toGoalBaseSteps(num, gb)
        res = ""
        for step in steps:
            res = res + step[3]
        return revString(res)


# bring everything together
def convert(num, b, g):
    num = str(num)
    # convert input num from base b to base 10
    numInb10 = sourceBaseToBase10(num, b)
    # convert num in base ten to base g
    numInBaseg = base10toGoalBase(numInb10, g)
    return numInBaseg


# Examples

print(convert("11111011", bin, decAlphaUp))
print(convert('0', dec, alpha))
print(convert("1234", dec, rev))
