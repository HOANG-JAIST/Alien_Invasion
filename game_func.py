
import sys

import pygame
from bullet import Bullet

def check_keydown_events(event, g_set, screen, ship, bullets): #when the key is pressed
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    
    elif event.key == pygame.K_SPACE:
        fire_bullet(g_set, screen, ship, bullets)

        """
        # Create a new bullet 
        if len(bullets) < g_set.bullets_allowed: # limmit number of bullets 
            new_bullet = Bullet(g_set, screen, ship)
            # Add it to the bullets group
            bullets.add(new_bullet)
        """
def fire_bullet(g_set, screen, ship, bullets):
    """ Fire a bullet if limit not reached yet"""
    # Create a new bullet 
    if len(bullets) < g_set.bullets_allowed: # limmit number of bullets 
        new_bullet = Bullet(g_set, screen, ship)
            # Add it to the bullets group
        bullets.add(new_bullet)

def check_keyup_events(event, ship): # when the key is released
    """Respond to key release"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(g_set, screen, ship, bullets):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, g_set, screen, ship, bullets)
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
def update_screen(g_set, screen, ship, bullets):
    """Update images on the screen and flip to the new screen"""
    
    #Redraw the screen during each pass via the loop
    screen.fill(g_set.bg_color)

    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites(): # bullets.sprites() method returns a list of all sprites in the group bullets
        bullet.draw_bullet()

    ship.blitme()

    #Make the most recently draw screen visible
    pygame.display.flip()

def update_bullets(bullets):
    """ Update position of bullets and get rid of old bullets"""
    # Update bullet position
    bullets.update()

    # Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)