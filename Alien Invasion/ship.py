import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """A class to manage the player's ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen              # Reference to the main game screen
        self.settings = ai_game.settings          # Access to game settings (like speed)
        self.screen_rect = ai_game.screen.get_rect()  # Rectangle representing the screen boundaries

        # Load the ship image and get its rect (rectangle area).
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store the ship's exact horizontal position as a float
        # (more precise than using just rect.x which is an int).
        self.x = float(self.rect.x)

        # Movement flags — track whether the ship is moving.
        # These are controlled by key presses in the event loop.
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        """Center the ship on the screen (used after losing a life)."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)  # Reset position tracker

    def update(self):
        """Update the ship's position based on movement flags."""
        # Move right if flag is set and ship is not at right edge.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        # Move left if flag is set and ship is not at left edge.
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect.x from self.x (sync float position with rect).
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location on the screen."""
        self.screen.blit(self.image, self.rect)
