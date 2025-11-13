import plotly.express as px   # Import Plotly Express for creating charts
from die import Die           # Import the Die class

# Create two dice: a standard six-sided die (D6) and a ten-sided die (D10)
die_1 = Die()        # Defaults to 6 sides
die_2 = Die(10)      # Explicitly create a die with 10 sides

# Roll both dice 50,000 times and store the sum of each roll
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()  # Roll both dice and add results
    results.append(result)                # Save the combined result

# Analyze the results:
# Count how many times each possible outcome occurs
frequencies = []
max_result = die_1.num_sides + die_2.num_sides   # Largest possible roll (6 + 10 = 16)
poss_results = range(2, max_result + 1)          # Possible outcomes range from 2 to 16

for value in poss_results:
    frequency = results.count(value)             # Count how many times "value" occurred
    frequencies.append(frequency)

# Visualize the results with a bar chart
title = "Results of Rolling a D6 and a D10 50,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}

# Create a bar chart:
# - x-axis: possible sums (2–16)
# - y-axis: frequency of each sum
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart:
# - Show every integer result on the x-axis (no skipped values)
fig.update_layout(xaxis_dtick=1)

# Display the chart in a browser window
fig.show()
