import pygame

from Setting import Settings


class Ship:
    def __init__(self, ai_settings: Settings, screen):
        self.screen = screen

        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moveing_right = False
        self.moveing_left = False

    def update(self):
        if self.moveing_right:
            self.rect.centerx += 1
        if self.moveing_left:
            self.rect.centerx -= 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)
