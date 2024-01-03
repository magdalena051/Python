# make a plot of cubes of numbers from 1-5, and of numbers from 1-5000
# version 1: combine both subplots in one plot
# how to set the axis range (start from 0) when using subplots?


import matplotlib.pyplot as plt


x1 = [0, 1, 2, 3, 4, 5]
y1 = [x**3 for x in x1]

x2 = list(range(1, 5001))
y2 = [x**3 for x in x2]


figure, ax = plt.subplots(2, 1)


ax[0].plot(x1, y1, linewidth=2)
ax[0].set_title("Cube numbers")
ax[0].set(xlabel="value", ylabel="cube of value")


ax[1].plot(x2, y2, linewidth=2)
ax[1].set_title("Cube numbers")
ax[1].set(xlabel="value", ylabel="cube of value")


# so that the plots don't overlap
plt.tight_layout()

plt.show()