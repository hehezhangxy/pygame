import pygame
from pygame.sprite import Group

import game_functions as gf
from Setting import Settings
from ship import Ship
from alien import Alien


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien")

    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Alien(ai_settings, screen)
    # gf.creat_fleet(ai_settings, screen, aliens)

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
