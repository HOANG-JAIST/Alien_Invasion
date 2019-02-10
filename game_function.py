
import sys 
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from setting import Settings

settings = Settings()

def check_keydown_events(event, settings, screen, ship, bullets): 
    """
    Respond to keypresses
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
       
def fire_bullet(settings, screen, ship, bullets):
    """ 
    Fire a bullet if limit not reached yet
    """
    if len(bullets) < settings.bullets_allowed: 
        new_bullet = Bullet(settings, screen, ship)
            # Add it to the bullets group
        bullets.add(new_bullet)

def check_keyup_events(event, ship): # when the key is released
    """
    Respond to key release
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """
    Respond to keypresses and mouse events
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(settings, screen, stats, sb, play_button, aliens, ship, bullets, mouse_x, mouse_y)

def check_play_button(settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """
    Start a New game when player click Play button
    """
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game statistics
        stats.reset_stats()
        stats.game_active = True

        # Reset the scoreboard image
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        # Create a new flet and center the ship
        create_fleet(settings, screen, ship, aliens)
        ship.center_ship()

def update_bullets(settings, screen, stats, sb, ship, aliens, bullets):
    """ 
    Update position of bullets and get rid of old bullets
    """
    # Update bullet position
    bullets.update()
    # Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    check_bullet_alien_collisions(settings, screen, stats, sb, ship, aliens, bullets)

def check_bullet_alien_collisions(settings, screen, stats, sb, ship, aliens, bullets):
    """ 
    Respond to bullet-alien collisions
    """
    # Remove any bullets and aliens that have collided
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.value():
            stats.score += settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

        # Increase level
        stats.level += 1
        sb.prep_level()

    if len(aliens) == 0:
        # Destroy existing bullets and create new fleet
        bullets.empty()
        create_fleet(settings, screen, ship, aliens)

def get_number_aliens_x(settings, alien_width):
    """ 
    Determine the number of aliens that fit in a row
    """
    available_space_x = settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(settings, ship_height, alien_height):
    """ 
    Determine the number of rows of aliens that fit on the screen
    """
    available_space_y = settings.screen_height - 2 * alien_height - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(settings, screen, aliens, alien_number, row_number):
    """ 
    Create an alien and place it in the row
    """
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(settings, screen, ship, aliens):
    """ 
    Create a fleet of aliens
    """
    alien = Alien(settings, screen)
    number_aliens_x = get_number_aliens_x(settings, alien.rect.width)
    number_rows = get_number_rows(settings, ship.rect.height, alien.rect.height)

    # Create the fleet of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(settings, screen, aliens, alien_number, row_number)
          
def update_screen(settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """ 
    Update images on the screen and flip to the new screen
    """
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites(): 
        bullet.draw_bullet()
    
    # Draw a button when the game is inactive
    if not stats.game_active:
        play_button.draw_button()

    ship.blitme()
    aliens.draw(screen)

    # Draw score information
    sb.show_score()

    #Make the most recently draw screen visible
    pygame.display.flip()

def check_fleet_edges(settings, aliens):
    """ 
    Respond appropriately if any aliens have reached an edge
    """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break

def change_fleet_direction(settings, aliens):
    """ 
    Drop the entire fleet and change the fleet's direction
    """
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1

def ship_hit(settings, stats, sb, screen, ship, aliens, bullets):
    """ 
    Respond to ship being hit by alien
    """
    if stats.ships_left > 0:
        # Decrement ships left
        stats.ships_left -= 1

        # Update scoreboard
        sb.prep_ships()

        # Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship
        create_fleet(settings, screen, ship, aliens)
        ship.center_ship()

        # Pause
        sleep(0.5)
    else:
        stats.game_active = False

def check_aliens_bottom(settings, stats, sb, screen, ship, aliens, bullets):
    """ 
    Check if any aliens have reached the bottom of the screen
    """
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit
            ship_hit(settings, stats, sb, screen, ship, aliens, bullets)
            break

def update_aliens(settings, stats, sb, screen, ship, aliens, bullets):
    """ 
    Check if the fleet is at an edge, and then update the position of all aliens in the fleet
    """
    check_fleet_edges(settings, aliens)
    aliens.update()

    # Look for alien-ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, stats, sb, screen, ship, aliens, bullets)

    # Look for aliens hitting the bottom of the screen
    check_aliens_bottom(settings, stats, sb, screen, ship, aliens, bullets)

def check_high_score(stats, sb):
    """
    Check to see if there is a new high score
    """
    if stats.core > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

