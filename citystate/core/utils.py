import pygame

from typing import (
    List
)
import os
from pathlib import Path


def get_project_root() -> Path:
    """Returns project root folder."""
    return Path(__file__).parent.parent


def load_image(file: str) -> pygame.Surface:
    """
    loads an image, prepares it for play
    """
    file = os.path.join(get_project_root(), 'assets', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s' % (file, pygame.get_error()))
    return surface.convert()


def load_images(*files: List[str]) -> pygame.Surface:
    imgs = []
    for file in files:
        imgs.append(load_image(file))
    return imgs


class dummysound:
    def play(self): pass


def load_sound(file: str) -> pygame.mixer.Sound:
    if not pygame.mixer: return dummysound()
    file = os.path.join(main_dir, 'data', file)
    try:
        sound = pygame.mixer.Sound(file)
        return sound
    except pygame.error:
        print('Warning, unable to load, %s' % file)
    return dummysound()
