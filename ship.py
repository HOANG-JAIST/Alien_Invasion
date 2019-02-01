
import pygame

class Ship():

    def __init__(self, g_set, screen):
        """Initialize ship and locate its starting position."""
        self.screen = screen
        
        #Ship will have access to its speed setting
        self.g_set = g_set 

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

        #Store decimal value for the ship's center
        self.center = float(self.rect.centerx)

        #Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag"""
        #Update the ship's center value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.g_set.ship_speed_factor 

        if self.moving_left and self.rect.left > 0:
            self.center -= self.g_set.ship_speed_factor

        #Update rect object from self.center
        self.rect.centerx = self.center

        

    # blitme method will draw the image to the screen @position specified by self.rect
    def blitme(self):
        """Draw the ship at its current position"""
        self.screen.blit(self.image, self.rect)
