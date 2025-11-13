import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a rectangle (rect) that represents the bullet.
        # The bullet is not an image, so we make it as a rectangle shape.
        self.rect = pygame.Rect(
            0, 0,
            self.settings.bullet_width,     # Width from settings.py
            self.settings.bullet_height     # Height from settings.py
        )

        # Position the bullet at the top-center of the ship.
        # This makes it look like bullets shoot from the ship's nose.
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's vertical position as a float
        # (for more precise, smooth movement).
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # Bullets travel upward, so we subtract from y-coordinate.
        self.y -= self.settings.bullet_speed

        # Update the rectangle’s position from the float value.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen as a filled rectangle."""
        pygame.draw.rect(self.screen, self.color, self.rect)
