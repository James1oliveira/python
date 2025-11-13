import plotly.express as px   # Import Plotly Express for easy charting
from die import Die           # Import the Die class

# Create two D6 dice (each has 6 sides by default)
die_1 = Die()
die_2 = Die()

# Roll both dice 1,000 times and store the sum of each roll
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()  # Roll both dice and add the values
    results.append(result)                # Save the result

# Analyze the results:
# Find out how many times each possible sum appears
frequencies = []  
max_result = die_1.num_sides + die_2.num_sides   # Largest possible result (6+6=12)
poss_results = range(2, max_result + 1)          # Possible results are 2 through 12

for value in poss_results:
    frequency = results.count(value)             # Count occurrences of each result
    frequencies.append(frequency)

# Visualize the results with a bar chart
title = "Results of Rolling Two D6 Dice 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}  # Axis labels

# Create bar chart:
# - x-axis: possible results (2–12)
# - y-axis: frequency (how many times each result occurred)
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart:
# - Force x-axis ticks to show every integer (2, 3, 4, …, 12)
fig.update_layout(xaxis_dtick=1)

# Show the chart in the browser
fig.show()
