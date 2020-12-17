import sys
import pygame

from Setting import Settings
from alien import Alien
from bullet import Bullet
from ship import Ship
from pygame.sprite import Group


def check_keydown_events(event, ai_settings: Settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moveing_right = True
    elif event.key == pygame.K_LEFT:
        ship.moveing_left = True
    elif event.key == pygame.K_SPACE:
        if len(bullets) < ai_settings.bullet_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moveing_right = False
    elif event.key == pygame.K_LEFT:
        ship.moveing_left = False


def check_events(ai_settings: Settings, screen, ship: Ship, bullets: Group()):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, aliens, bullets: Group()):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()


def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def creat_fleet(ai_settings: Settings, screen: pygame.Surface, aliens):
    alien = Alien(ai_settings, screen)
    alien_with = alien.rect.width
    aviliable_space_x = ai_settings.screen_width - 2 * alien_with
    number_aliens_x = int(aviliable_space_x / (2 * alien_with))

    for alien_number in range(number_aliens_x):
        alien = Alien(ai_settings, screen)
        alien.x = alien_with + 2 * alien_with * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)

