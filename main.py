# import modules
import sys # to exist the game when player quits
import pygame

#Khai bao abstract class
from setting import Settings
from ship import Ship

def run_game():
    # Initialize pygame, settings, and screen object
    # initialize background setting    
    pygame.init() 

    #khoi tao class
    g_set = Settings() 

    # create a display window called screen with screen_width pixels, sreen_hight pixels
    screen = pygame.display.set_mode((g_set.scr_width, g_set.scr_hight)) 
    pygame.display.set_caption("Alien-Invasion by Anhh")

    # Make a ship
    ship = Ship(screen)


    # set background color, store in bg_color
    # bg_color = (150, 150, 150) # (R,G,B = [0,255])

    # main loop for game
    while True:

        # watch for keyboard and mouse event
        # an event loop; event is an action that player performs while playing game
        # access the event detected by Pygame
        for event in pygame.event.get(): 
           if event.type == pygame.QUIT:
                sys.exit()
    
        # redraw screen during each pass via loop, fill screen with bg_color
        screen.fill(g_set.bg_color) 

        ship.blitme()

        # make the the most recently draw screen visible
        # update display
        pygame.display.flip() 

run_game() 

