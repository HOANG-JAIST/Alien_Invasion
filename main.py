# Alien-Invasion game

import pygame
from pygame.sprite import Group 

from setting import Settings
from ship import Ship
from alien import Alien
import game_func as gf 

def run_game():
    pygame.init() 
    g_set = Settings() 

    # Create a display window 
    screen = pygame.display.set_mode((g_set.scr_width, g_set.scr_height)) 
    pygame.display.set_caption("Alien-Invasion by Anhh")

    # Make a ship
    ship = Ship(g_set, screen)

    # Make a group of bullets, group of aliens 
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens
    gf.create_fleet(g_set, screen, ship, aliens)

    while True:
        gf.check_events(g_set, screen, ship, bullets) 
        ship.update() 
        gf.update_bullets(bullets)
        gf.update_screen(g_set, screen, ship, aliens, bullets) 

run_game() 

