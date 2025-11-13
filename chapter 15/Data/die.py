from random import randint  # Import randint function to generate random integers

class Die:
    """A class representing a single die."""

    def __init__(self, num_sides=6):
        """
        Initialize the die.
        
        Args:
            num_sides (int): The number of sides the die should have.
                             Defaults to 6 (a standard die).
        
        Each die object will remember how many sides it has.
        """
        self.num_sides = num_sides  # Save the number of sides for this die

    def roll(self):
        """
        Simulate rolling the die.

        Returns:
            int: A random integer between 1 and the number of sides (inclusive).
        """
        return randint(1, self.num_sides)  # Generate and return a random roll
