# Create a tribonacci function that given a signature array/list, returns the 
# first n elements - signature included - of the so seeded sequence.
# Input is assumed to be correct - signature will always contain 3 numbers; n
# will always be a non-negative number; if n == 0, then return an empty array
#
# Task source: https://www.codewars.com/kata/556deca17c58da83c00002db


def tribonacci(sig, n):
    if n==0:
        tri = []
        return tri
    elif n==1:
        tri = [sig[0]]
        return tri
    elif n==2:
        tri = [sig[0], sig[1]]
        return tri
    elif n>=3:
        tri = [sig[0], sig[1], sig[2]]
        temp = [sig[0], sig[1], sig[2]]
        for i in range(3,n):    # range includes first number, excludes last number
            nextVal = temp[2] + temp[1] + temp[0]
            tri.append(nextVal)
            temp[0] = tri[i-2]
            temp[1] = tri[i-1]
            temp[2] = tri[i]
        return tri
    

# Example
print(tribonacci([1,1,1], 10))

