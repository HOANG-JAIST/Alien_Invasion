# Bullet Class

import pygame
from pygame.sprite import Sprite 

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""
    
    def __init__(self, g_set, screen, ship):
        """Create a bullet object at the ship's current position"""
        super().__init__() 
        self.screen = screen

        # Bullet position
        self.rect = pygame.Rect(0, 0, g_set.bullet_width, g_set.bullet_height) 
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top 

        # for decimal value 
        self.y = float(self.rect.y) 

        self.color = g_set.bullet_color
        self.speed_factor = g_set.bullet_speed_factor

    def update(self): 
        """ Move the bullet up to screen"""
        # Update bullet position
        self.y -= self.speed_factor 
        self.rect.y = self.y

    def draw_bullet(self): 
        pygame.draw.rect(self.screen, self.color, self.rect)