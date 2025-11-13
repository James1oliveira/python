class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static (unchanging) settings."""
        # --- Screen settings ---
        self.screen_width = 1200   # Window width
        self.screen_height = 800   # Window height
        self.bg_color = (230, 230, 230)  # Light gray background

        # --- Ship settings ---
        self.ship_limit = 3  # Number of lives/ships the player has

        # --- Bullet settings ---
        self.bullet_width = 3      # Bullet thickness
        self.bullet_height = 15    # Bullet length
        self.bullet_color = (60, 60, 60)  # Dark gray bullets
        self.bullets_allowed = 3   # Max bullets allowed on screen at once

        # --- Alien settings ---
        self.fleet_drop_speed = 10  # How far the fleet drops down when reaching an edge

        # --- Game speed scaling ---
        self.speedup_scale = 1.1  # Factor by which speed increases each level
        self.score_scale = 1.5    # Factor by which alien point values increase

        # Initialize dynamic (changing) settings
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change during the game."""
        # Speeds
        self.ship_speed = 1.5     # Initial ship movement speed
        self.bullet_speed = 2.5   # Initial bullet speed
        self.alien_speed = 1.0    # Initial alien movement speed

        # Fleet direction:
        #   1 = moving right
        #  -1 = moving left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50  # Initial points per alien

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        # Speeds gradually get faster with each new level
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        # Alien point value increases too (to reward higher difficulty)
        self.alien_points = int(self.alien_points * self.score_scale)
