
import pygame

class Ship():

    def __init__(self, screen):
        """Initialize ship and locate its starting position."""
        self.screen = screen

        # Load ship image will return a surface representing the ship, and store in self.image
        self.image = pygame.image.load('images/ship.bmp')

        # Game elements like rectangles (rects)
        self.rect = self.image.get_rect()

        # Store the screen's rect 
        self.screen_rect = screen.get_rect()

        # Start new ship at bottom center of screen
        # x-coordinate of the ship's center match the centerx attribute of the screen's rect (same for y-coordinate!)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    # blitme method will draw the image to the screen @position specified by self.rect
    def blitme(self):
        """Draw the ship at its current position"""
        self.screen.blit(self.image, self.rect)
