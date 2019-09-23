from collections import defaultdict
import random

import pygame

from citystate.core.constants import SCREEN_RECT
from citystate.core.utils import load_image


class City(pygame.sprite.Sprite):
    def __init__(self, containers):
        pygame.sprite.Sprite.__init__(self, containers)
        self.width = 32
        self.height = 32
        self.image = pygame.transform.scale(load_image('city.png'), (self.width, self.height))
        self.rect = self.image.get_rect()
        self.owner = None
        self.occupiers = defaultdict(int)  # [player: count]
        self.rect.x = (SCREEN_RECT.width - self.width) * random.random()
        self.rect.y = (SCREEN_RECT.height - self.height) * random.random()

    def occupied(self, player) -> bool:
        if self.occupiers[player] == 0:
            self.occupiers[player] += 1
            self.owner = player
            return True
        return False
