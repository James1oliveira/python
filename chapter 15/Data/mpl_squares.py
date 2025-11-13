import matplotlib.pyplot as plt  # Import Matplotlib for plotting

# Data to plot
squares = [1, 4, 9, 16, 25]        # y-values (squares of numbers)
input_values = [1, 2, 3, 4, 5]     # x-values

# Use a predefined style for the plot
plt.style.use('seaborn-v0_8')

# Create a figure and axes object
fig, ax = plt.subplots()

# Plot data: input_values on x-axis, squares on y-axis
ax.plot(input_values, squares, linewidth=3)

# Plot squares again, but this time using only y-values (x defaults to index)
# This will create a second line on the same chart
ax.plot(squares, linewidth=3)

# Set chart title and axis labels
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Adjust size of tick labels for readability
ax.tick_params(labelsize=14)

# Display the plot
plt.show()
