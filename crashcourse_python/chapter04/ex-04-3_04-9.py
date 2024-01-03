
# ex 4-3
# print all numbers between 1 and 20 (inclusive)
for num in range(1,21):
    print(num)
print("\n")
    
# ex 4-5
# make a list of numbers between 1 and 1 million, check that it
# indeed starts at 1 and ends at 1 million, and sum up all the entries
mil = list(range(1,1000001))
print(min(mil))
print(max(mil))
print(sum(mil))
print("\n")

# ex 4-6
# print all uneven numbers between 1 and 20 using the step size argument in range()
for num in range(1,20,2):
    print(num)
print("\n")
    
# ex 4-7
# print all multiples of 3 between 1 and 30 using the step size argument
for num in range(3,31,3):
    print(num)
    
# make a list of multiples of 3 of numbers from 1 to 30 in list notation
multofthree = [num for num in range(3,31,3)]
print(multofthree)
print("\n")

# ex 4-8
# make a list of all cubes of numbers from 1 to 10 
cubes = []
for num in range(1,11):
    cubes.append(num**3)
print(cubes)
print("\n")

# ex 4-9
# do the same thing in list notation
cubes2 = [num**3 for num in range(1,11)]
print(cubes2)
