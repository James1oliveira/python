import matplotlib.pyplot as plt

# Generate data
x_values = range(1, 1001)                  # x-axis values: numbers 1 through 1000
y_values = [x**2 for x in x_values]        # y-axis values: squares of numbers

# Choose a style for the plot
plt.style.use('seaborn-v0_8')

# Create the figure and axes object
fig, ax = plt.subplots()

# Create a scatter plot:
# - x_values on the x-axis, y_values on the y-axis
# - c=y_values colors the points based on their y-value
# - cmap=plt.cm.Blues applies a blue color gradient (lighter for small values, darker for large values)
# - s=10 makes the points small
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and axis labels
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Adjust size of tick labels
ax.tick_params(labelsize=14)

# Plot a single point at (2, 4) to highlight it (example point)
ax.scatter(2, 4)

# Set axis ranges:
# - x-axis: 0 to 1100
# - y-axis: 0 to 1,100,000
ax.axis([0, 1100, 0, 1_100_000])

# Format tick labels in plain style (instead of scientific notation)
ax.ticklabel_format(style='plain')

# Show the plot
plt.show()
