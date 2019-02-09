# Ship class

import pygame

class Ship():

    def __init__(self, settings, screen):
        """
        Initialize ship and locate its starting position
        """
        self.screen = screen
        self.settings = settings 
        self.image = pygame.image.load('images/ship.bmp')

        # Game elements (rects)
        self.rect = self.image.get_rect()

        # Store the screen's rect 
        self.screen_rect = screen.get_rect()

        # Start new ship at bottom center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # for decimal value
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """
        Update the ship's position based on the movement flag
        """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor 

        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed_factor

        # Update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """
        Draw the ship at its current position
        """
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """ 
        Center the ship on the screen
        """
        self.center = self.screen_rect.centerx
