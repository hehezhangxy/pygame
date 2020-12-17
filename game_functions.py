import sys
import pygame

from ship import Ship


def check_events(ship: Ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moveing_right = True
            elif event.key == pygame.K_LEFT:
                ship.moveing_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moveing_right = False
            elif event.key == pygame.K_LEFT:
                ship.moveing_left = False


def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()
