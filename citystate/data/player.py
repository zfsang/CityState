import pygame
from citystate.core.constants import SCREENRECT

from citystate.core.utils import load_image


class Player(pygame.sprite.Sprite):
    speed = 10
    images = []

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = load_image('spartan')
        self.rect = self.image.get_rect()
        self.reloading = 0
        self.origtop = self.rect.top
        self.facing = -1

    def move(self, direction):
        self.rect = self.rect.move(direction * self.speed, 0).clamp(SCREENRECT)
