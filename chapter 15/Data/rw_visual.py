import matplotlib.pyplot as plt
from random_walk import RandomWalk  # Import the RandomWalk class

while True:
    # Create a random walk with 50,000 points
    rw = RandomWalk(50_000)
    rw.fill_walk()  # Generate the walk data (x and y coordinates)

    # Set the plot style and create the figure and axes
    plt.style.use('classic')
    fig, ax = plt.subplots()

    # Generate a sequence of point numbers for coloring the walk
    point_numbers = range(rw.num_points)

    # Plot all the points with a color gradient (Blues colormap)
    # - x and y values from the walk
    # - color depends on order of points (earlier = lighter, later = darker)
    # - edgecolors='none' removes black edges around points
    # - s=1 makes points very small (so 50k can fit nicely)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
               edgecolors='none', s=1)

    # Alternative plotting: Uncomment this to plot points in one color
    # ax.scatter(rw.x_values, rw.y_values, s=15)

    # Make sure the aspect ratio is equal so steps look correct (not stretched)
    ax.set_aspect('equal')

    # Emphasize the start and end points of the walk (optional)
    # Uncomment below if you want to highlight them:
    # ax.scatter(0, 0, c='green', edgecolors='none', s=100)  # Starting point
    # ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)  # Ending point

    # Hide the axes for a cleaner look
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # Display the plot
    plt.show()

    # Ask user if they want to generate another walk
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break  # Exit loop if user chooses not to continue
