# Alien-Invasion game

import pygame
from pygame.sprite import Group
from setting import Settings
import game_function as gf 
from game_stats import GameStats
from ship import Ship
from button import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init() 
    settings = Settings() 

    # Create a display window 
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height)) 
    pygame.display.set_caption("First_Game by Anhh")

    # Make a play button
    play_button = Button(settings, screen, "Play")

    # Create an instance to store game statistics and create a scoreboard
    stats = GameStats(settings)
    sb = Scoreboard(settings, screen, stats)

    # Make a ship
    ship = Ship(settings, screen)

    # Make a group of bullets, group of aliens 
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens
    gf.create_fleet(settings, screen, ship, aliens)

    while True:
        gf.check_events(settings, screen, stats, play_button, aliens, ship, bullets) 
        if stats.game_active:
                ship.update() 
                gf.update_bullets(settings, screen, ship, aliens, bullets)
                gf.update_aliens(settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(settings, screen, stats, sb, ship, aliens, bullets, play_button) 

run_game()

