# Creating the Bullet Class, which inherits from Sprite
import pygame
from pygame.sprite import Sprite # Sprite can help to group related elements in the game and act on the grouped elements at once

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    # __init__ needs the g_set, screen, and ship instance
    def __init__(self, g_set, screen, ship):
        """Create a bullet object at the ship's current position"""
        super().__init__() #for Python 2.7, it works on Python 3 too. same as super().__init__()
        self.screen = screen

        # Create a bullet rect at (0, 0) 
        self.rect = pygame.Rect(0, 0, g_set.bullet_width, g_set.bullet_height) # Bullet is not based on image so we build a rect from scratch

        # then set (move to) correct position
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top # bullet is fired from the ship

        # Store the bullet's position as a decimal value for fine adjustments to the bullet's speed
        self.y = float(self.rect.y) 

        self.color = g_set.bullet_color
        self.speed_factor = g_set.bullet_speed_factor

    def update(self): # Method to manage bullet's position
        """ Move the bullet up to screen"""
        # Update decimal position of the bullet
        self.y -= self.speed_factor # when bullet is fired, it move up the screen. We need subtract the amount stored in self.speed_factor from self.y
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self): # Method to draw a bullet on the screen
        pygame.draw.rect(self.screen, self.color, self.rect)