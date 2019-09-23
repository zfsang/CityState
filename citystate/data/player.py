import pygame

from citystate.core.constants import SCREEN_RECT
from citystate.core.utils import load_image


class Player(pygame.sprite.Sprite):
    def __init__(self, containers):
        pygame.sprite.Sprite.__init__(self, containers)
        self.image = pygame.transform.scale(load_image('spartan.gif'), (32, 32))
        self.rect = self.image.get_rect()
        self.reloading = 0
        self.orig_top = self.rect.top
        self.facing = -1
        self.speed = 7
        self.cities_count = 0

    def move(self, direction_x, direction_y):
        self.rect = self.rect.move(direction_x * self.speed, direction_y * self.speed).clamp(SCREEN_RECT)

    def occupy_city(self):
        self.cities_count += 1
