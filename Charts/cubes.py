import matplotlib.pyplot as plt

x_values = list(range(1, 10))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, edgecolor = 'none', s = 40)

# Set chart title and axes.
plt.title("Cubed numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Cube of value", fontsize = 14)

# Set size of tick labels
plt.tick_params(axis = 'both', which = 'major', labelsize = 11)

plt.axis([0, 10, 0, 750])
plt.show()
