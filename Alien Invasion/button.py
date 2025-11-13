import pygame.font


class Button:
    """A class to build buttons for the game (e.g., Play button)."""

    def __init__(self, ai_game, msg):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()  # Screen boundaries

        # Set the dimensions and styling of the button
        self.width, self.height = 200, 50                # Button size
        self.button_color = (0, 135, 0)                  # Green background
        self.text_color = (255, 255, 255)                # White text
        self.font = pygame.font.SysFont(None, 48)        # Default font, size 48

        # Create a rectangle for the button and center it on the screen
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Prepare the button's label (text) once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """
        Turn the text message (msg) into an image
        and center it on the button.
        """
        # Render the text into an image
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.button_color
        )

        # Get the rectangle of the rendered text
        self.msg_image_rect = self.msg_image.get_rect()

        # Center the text image inside the button rectangle
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw the button rectangle and then the text message."""
        # Fill the button area with the background color
        self.screen.fill(self.button_color, self.rect)

        # Draw (blit) the text image on top of the button
        self.screen.blit(self.msg_image, self.msg_image_rect)
