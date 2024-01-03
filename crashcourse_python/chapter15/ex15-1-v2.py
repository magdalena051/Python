# make a plot of cubes of numbers from 1-5, and of numbers from 1-5000
# version 2: make two separate plots, comment out as needed

import matplotlib.pyplot as plt


x1 = [0, 1, 2, 3, 4, 5]
y1 = [x**3 for x in x1]

x2 = list(range(1, 5001))
y2 = [x**3 for x in x2]


#plt.plot(x1, y1, linewidth=3)
plt.scatter(x2, y2, c=y2, cmap=plt.cm.Blues, edgecolor="none", s=5)
plt.title("Cube numbers")
plt.xlabel("value")
plt.ylabel("cube of value")


# set axis ticks
plt.tick_params(axis="both", which="major", labelsize=14)

# set the axis range
#plt.axis([0, 5, 0, 130])
plt.axis([0, 5001, 0, 5001**3])

plt.show()

