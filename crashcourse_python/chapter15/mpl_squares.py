
import matplotlib.pyplot as plt 

input_values = [1, 2, 3, 4, 5]
output_values = [1, 4, 9, 16, 25]

plt.plot(input_values, output_values, linewidth=3)


# set the plot title and axis labels
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# set the size of the axis points
plt.tick_params(axis="both", labelsize=14)


# this needs to come at the end
plt.show()

