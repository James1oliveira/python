import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()  
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image from the images folder
        # and get its rectangular area (used for positioning).
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top-left corner of the screen.
        # Position is set to one alien-width and one alien-height away
        # from the top-left corner so it doesn’t spawn off-screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's precise horizontal position (float)
        # This allows smoother movement compared to using only integers.
        self.x = float(self.rect.x)

    def check_edges(self):
        """
        Return True if alien is at the edge of the screen.
        Used by the fleet to decide when to change direction.
        """
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Move the alien right or left depending on fleet direction."""
        # Fleet direction is 1 for right, -1 for left
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x  # Update rect position based on float x
