class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings

        # Call reset_stats() so game stats start fresh at the beginning
        self.reset_stats()

        # High score should never be reset between games
        self.high_score = 0

    def reset_stats(self):
        """
        Initialize statistics that can change during the game.
        Called when a new game starts.
        """
        # Number of ships (lives) left for the player
        self.ships_left = self.settings.ship_limit

        # Player's score starts at 0
        self.score = 0

        # Player starts on level 1
        self.level = 1
