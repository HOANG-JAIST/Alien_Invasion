# Alien-Invasion game

import pygame
from pygame.sprite import Group 

from setting import Settings
from ship import Ship

import game_func as gf 

def run_game():
    # Initialize pygame, settings, and screen object  
    pygame.init() 

    g_set = Settings() 

    # Create a display window 
    screen = pygame.display.set_mode((g_set.scr_width, g_set.scr_hight)) 
    pygame.display.set_caption("Alien-Invasion by Anhh")

    # Make a ship
    ship = Ship(g_set, screen)

    # Make a group to store bullets in 
    bullets = Group() 


    # set background color, store in bg_color
    # bg_color = (150, 150, 150) # (R,G,B = [0,255])

    # Main loop for game
    while True:
        gf.check_events(g_set, screen, ship, bullets) # check for the main input
        ship.update() # update ship's position
        #bullets.update() 
        gf.update_bullets(bullets) # any bullets hahve been fired
        
        """# Get rid of bullets that have disappeared
        for bullet in bullets.copy(): # copy() method to set up for loop
                if bullet.rect.bottom <= 0: # check whether bullets disappeared off the top of scr
                        bullets.remove(bullet)
        #print(len(bullets))
        """

        gf.update_screen(g_set, screen, ship, bullets) # draw new screen

        """Refactoring
        # watch for keyboard and mouse event
        # an event loop; event is an action that player performs while playing game
        # access the event detected by Pygame
        for event in pygame.event.get(): 
           if event.type == pygame.QUIT:

                # to exist the game when player quits
                sys.exit()
        """
        """
        # redraw screen during each pass via loop, fill screen with bg_color
        screen.fill(g_set.bg_color) 

        ship.blitme()

        # make the the most recently draw screen visible
        # update display
        pygame.display.flip() 
        """

run_game() 

