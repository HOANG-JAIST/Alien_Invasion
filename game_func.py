
import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, g_set, screen, ship, bullets): 
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(g_set, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
       
def fire_bullet(g_set, screen, ship, bullets):
    """ Fire a bullet if limit not reached yet"""
    if len(bullets) < g_set.bullets_allowed: 
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
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_bullets(bullets):
    """ Update position of bullets and get rid of old bullets"""
    # Update bullet position
    bullets.update()
    # Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def get_number_aliens_x(g_set, alien_width):
    """ Determine the number of aliens that fit in a row"""
    available_space_x = g_set.scr_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(g_set, ship_height, alien_height):
    """ Determine the number of rows of aliens that fit on the screen"""
    available_space_y = g_set.scr_height - 2 * alien_height - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(g_set, screen, aliens, alien_number, row_number):
    """ Create an alien and place it in the row"""
    alien = Alien(g_set, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(g_set, screen, ship, aliens):
    """ Create a fleet of aliens"""
    alien = Alien(g_set, screen)
    number_aliens_x = get_number_aliens_x(g_set, alien.rect.width)
    number_rows = get_number_rows(g_set, ship.rect.height, alien.rect.height)

    # Create the fleet of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(g_set, screen, aliens, alien_number, row_number)
          
def update_screen(g_set, screen, ship, aliens, bullets):
    """ Update images on the screen and flip to the new screen"""
    screen.fill(g_set.bg_color)
    for bullet in bullets.sprites(): 
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    #Make the most recently draw screen visible
    pygame.display.flip()
