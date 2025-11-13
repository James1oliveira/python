import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard:
    """A class to report and display scoring information."""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for rendering text (score, level, etc.)
        self.text_color = (30, 30, 30)   # Dark gray text
        self.font = pygame.font.SysFont(None, 48)  # Default font, size 48

        # Prepare the initial images for score, high score, level, and lives
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Render the current score as an image."""
        # Round score to nearest 10 for cleaner display
        rounded_score = round(self.stats.score, -1)
        # Format score with commas (e.g., 1,000 instead of 1000)
        score_str = f"{rounded_score:,}"

        # Render text to an image
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color
        )

        # Position score at the top-right corner
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Render the high score as an image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"

        # Render text to an image
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.settings.bg_color
        )

        # Position high score centered at the top
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Render the current level as an image."""
        level_str = str(self.stats.level)

        # Render text to an image
        self.level_image = self.font.render(
            level_str, True, self.text_color, self.settings.bg_color
        )

        # Position level just below the score (top-right area)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Show how many ships (lives) the player has left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            # Create a mini ship icon for each life left
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def check_high_score(self):
        """Update high score if the current score is greater."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()  # Refresh image

    def show_score(self):
        """Draw score, high score, level, and remaining ships to the screen."""
        self.screen.blit(self.score_image, self.score_rect)          # Current score
        self.screen.blit(self.high_score_image, self.high_score_rect) # High score
        self.screen.blit(self.level_image, self.level_rect)          # Level
        self.ships.draw(self.screen)  # Small ship icons (lives left)
