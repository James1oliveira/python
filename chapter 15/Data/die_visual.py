import plotly.express as px   # Import Plotly Express for easy charting
from die import Die           # Import the Die class we created earlier

# Create a D6 (a standard six-sided die)
die = Die()

# Roll the die 1,000 times and store results in a list
results = []
for roll_num in range(1000):
    result = die.roll()      # Simulate a roll
    results.append(result)   # Store the outcome

# Analyze the results:
# Count how many times each possible die value appears
frequencies = []                               # Holds frequency for each side
poss_results = range(1, die.num_sides + 1)     # Possible results (1 through 6)
for value in poss_results:
    frequency = results.count(value)           # Count how often this value appears
    frequencies.append(frequency)              # Save the frequency

# Visualize the results with a bar chart
title = "Results of Rolling One D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}  # Axis labels

# Create a bar chart:
# - x-axis: possible die results (1–6)
# - y-axis: frequencies (how many times each value appeared)
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Show the chart in a browser window
fig.show()
