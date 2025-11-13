import sys
from time import sleep
import pygame

# Import other game modules (your own classes)
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()  # Control frame rate
        self.settings = Settings()        # Load game settings

        # Create the game screen (window)
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Create game stats and scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        # Create the player's ship, bullets group, and aliens group
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        # Build the initial alien fleet
        self._create_fleet()

        # Game starts in an inactive state (waiting for Play button)
        self.game_active = False

        # Create the Play button
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start the main game loop."""
        while True:
            # Handle input (keyboard/mouse)
            self._check_events()

            if self.game_active:
                # Update game objects only if game is active
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            # Redraw the screen each loop
            self._update_screen()
            self.clock.tick(60)  # Run at 60 FPS

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Close window
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if player clicked the Play button
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # Reset dynamic settings (speed, difficulty, etc.)
            self.settings.initialize_dynamic_settings()

            # Reset game statistics and scoreboard
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self.game_active = True

            # Clear bullets and aliens, then start fresh
            self.bullets.empty()
            self.aliens.empty()
            self._create_fleet()
            self.ship.center_ship()

            # Hide mouse cursor during play
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:  # Quit the game
            sys.exit()
        elif event.key == pygame.K_SPACE:  # Shoot bullet
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet if limit not reached."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update bullet positions and remove off-screen bullets."""
        self.bullets.update()

        # Remove bullets that move off the top of the screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # Check if bullets hit aliens
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that collide
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if collisions:
            # Award points for each alien destroyed
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            # If fleet is destroyed, make a new one and speed up
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Level up
            self.stats.level += 1
            self.sb.prep_level()

    def _ship_hit(self):
        """Handle the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Reduce lives and update scoreboard
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Reset bullets and aliens
            self.bullets.empty()
            self.aliens.empty()

            # Create new fleet and reset ship position
            self._create_fleet()
            self.ship.center_ship()

            # Brief pause
            sleep(0.5)
        else:
            # Game over
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _update_aliens(self):
        """Update alien fleet position and check for collisions."""
        self._check_fleet_edges()
        self.aliens.update()

        # Ship collision check
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Check if aliens reached bottom
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        """Check if aliens hit the bottom of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat as a ship being hit
                self._ship_hit()
                break

    def _create_fleet(self):
        """Create a grid of aliens."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        # Start positions for grid
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # New row
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """Create a single alien and place it in the fleet."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """Change fleet direction if any alien hits the edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop fleet down and reverse horizontal direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Redraw all elements and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)

        # Draw bullets, ship, and aliens
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        # Draw score/lives/level
        self.sb.show_score()

        # Draw play button if game inactive
        if not self.game_active:
            self.play_button.draw_button()

        # Flip to show latest frame
        pygame.display.flip()


if __name__ == '__main__':
    # Create game instance and start the game loop
    ai = AlienInvasion()
    ai.run_game()
