# Bullet Class

import pygame
from pygame import sprite 
from setting import Settings
class Bullet(sprite.Sprite):
    """
    A class to manage bullets fired from the ship
    """
    def __init__(self, settings, screen, ship):
        """
        Create a bullet object at the ship's current position
        """
        super().__init__() 
        self.screen = screen
        self.settings = Settings()

        # Bullet position
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height) 
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top 

        # for decimal value 
        self.y = float(self.rect.y) 

        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor

    def update(self): 
        """ 
        Move the bullet up to screen
        """
        self.y -= self.speed_factor 
        self.rect.y = self.y

    def draw_bullet(self): 
        pygame.draw.rect(self.screen, self.color, self.rect)