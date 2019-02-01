
import sys

import pygame

def check_keydown_events(event, ship):
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event, ship):
    """Respond to key release"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
            """if event.key == pygame.K_RIGHT:
                ship.moving_right = True
                #Move the ship to the right
                #ship.rect.centerx +=1
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
            """

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            """
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False

            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
            """
def update_screen(g_set, screen, ship):
    """Update images on the screen and flip to the new screen"""
    
    #Redraw the screen during each pass via the loop
    screen.fill(g_set.bg_color)
    ship.blitme()

    #Make the most recently draw screen visible
    pygame.display.flip()