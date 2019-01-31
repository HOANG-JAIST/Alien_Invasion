# import modules
import sys # to exist the game when player quits
import pygame

from settings import Settings

def run_game():
    # Initialize pygame, settings, and screen object
    pygame.init() # initialize background setting
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_hight)) # create a display window called screen with screen_width pixels, sreen_hight pixels
    pygame.display.set_caption("Alien Invasion by Anhh")

    # set background color, store in bg_color
    # bg_color = (150, 150, 150) # (R,G,B = [0,255])

    # main loop for game
    while True:

        # watch for keyboard and mouse event
        # an event loop; event is an action that player performs while playing game
        for event in pygame.event.get(): # access the event detected by Pygame
           if event.type == pygame.QUIT:
              sys.exit()
    
        # redraw screen during each pass via loop, fill screen with bg_color
        screen.fill(game_settings.bg_color) 

        # make the the most recently draw screen visible
        pygame.display.flip() # update display

run_game() # initialize the game and start the main loop

