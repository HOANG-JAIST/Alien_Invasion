# Ship class

import pygame

class Ship():

    def __init__(self, g_set, screen):
        """Initialize ship and locate its starting position"""
        self.screen = screen
        self.g_set = g_set 
        self.image = pygame.image.load('images/ship.bmp')

        # Game elements (rects)
        self.rect = self.image.get_rect()

        # Store the screen's rect 
        self.scr_rect = screen.get_rect()

        # Start new ship at bottom center of screen
        self.rect.centerx = self.scr_rect.centerx
        self.rect.bottom = self.scr_rect.bottom

        # for decimal value
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag"""
        if self.moving_right and self.rect.right < self.scr_rect.right:
            self.center += self.g_set.ship_speed_factor 

        if self.moving_left and self.rect.left > 0:
            self.center -= self.g_set.ship_speed_factor

        # Update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current position"""
        self.screen.blit(self.image, self.rect)
