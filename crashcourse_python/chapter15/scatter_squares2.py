# make a scatter plot of square numbers 

import matplotlib.pyplot as plt 


# define x- and y-values (using a loop)
x_values = list(range(1,1001))          # generate a list containing integers 1-1000 
y_values = [x**2 for x in x_values]     # list of square numbers with abbreviated for loop


# Create the scatter plot: Version 1
# edgecolor sets the border color of the dots, s sets the size of the dots
# color: set dot color, can use words (e.g. "blue" or RGB tuple; values near 0 
# are darker, values near 1 are lighter)
# plt.scatter(x_values, y_values, color=(0,0.8,0.8), edgecolor="none", s=3)

# Create the scatter plot: Version 2
# color-map the values (use "c" argument instead of "color" argument if values are 
# to be color-mapped)
# with plt.cm.Blues, points with small y-values are light blue and points with larger
# y-values are darker blue
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor="none", s=5)


# set the plot title and axis labels
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)


# set the size of the axis points
plt.tick_params(axis="both", which="major", labelsize=14)


# set the axis range
plt.axis([0, 1100, 0, 1100000])

# display the plot
plt.show()

# save the plot as a file (bbox_inches="tight" removes excess white space)
# plt.savefig("squares_plot.png", bbox_inches="tight")
