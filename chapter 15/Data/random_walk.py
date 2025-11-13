from random import choice  # Import choice() to randomly select from a list

class RandomWalk:
    """A class to generate random walks."""
    
    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points  # Total number of points in the walk
        
        # All walks start at the origin (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""
        
        # Keep taking steps until the walk reaches the desired length
        while len(self.x_values) < self.num_points:
            
            # Decide the direction (+1 = forward, -1 = backward) and distance (0–4) for the x-axis
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance  # Final x movement for this step
            
            # Decide the direction and distance for the y-axis
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance  # Final y movement for this step
            
            # Skip this loop if both steps are zero (no movement)
            if x_step == 0 and y_step == 0:
                continue
            
            # Calculate the new position by adding the step to the last point
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            
            # Append the new position to the walk
            self.x_values.append(x)
            self.y_values.append(y)
