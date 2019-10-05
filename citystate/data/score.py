import pygame
from pygame.locals import Color


class Score(pygame.sprite.Sprite):
    def __init__(self, containers):
        pygame.sprite.Sprite.__init__(self, containers)
        self.font = pygame.font.Font(None, 20)
        self.font.set_italic(1)
        self.color = Color('white')
        self.last_score = -1
        self.score = 0
        self.image = None
        self.update()
        self.rect = self.image.get_rect().move(10, 450)

    def update_score(self, score):
        self.score = score

    def update(self):
        if self.score != self.last_score:
            self.last_score = self.score
            msg = f"Score: {self.score}"
            self.image = self.font.render(msg, 0, self.color)
