# make a scatter plot of square numbers 

import matplotlib.pyplot as plt 

# define x- and y-values (here done manually)
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.scatter(x_values, y_values, s=10)

# set the plot title and axis labels
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)


# set the size of the axis points
plt.tick_params(axis="both", which="major", labelsize=14)

# display the plot
plt.show()