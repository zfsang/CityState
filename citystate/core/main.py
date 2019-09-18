import pygame
from pygame.locals import *
from citystate.core.utils import (
    load_image,
    load_images,
    load_sound
)
from citystate.data.player import Player

SCREENRECT = Rect(0, 0, 640, 480)


def main():
    # Initialize pg
    if pygame.get_sdl_version()[0] == 2:
        pygame.mixer.pre_init(44100, 32, 2, 1024)
    pygame.init()
    if pygame.mixer and not pygame.mixer.get_init():
        print('Warning, no sound')
        pygame.mixer = None

    fullscreen = False
    # Set the display mode
    winstyle = 0  # |FULLSCREEN
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)
    # create the background, tile the bgd image
    bgdtile = load_image('map.gif')
    background = pygame.Surface(SCREENRECT.size)
    for x in range(0, SCREENRECT.width, bgdtile.get_width()):
        background.blit(bgdtile, (x, 0))

        player = Player()
    screen.blit(background, (0, 0))
    pygame.display.flip()

    if pygame.mixer:
        pygame.mixer.music.fadeout(1000)
    pygame.time.wait(1000)
    pygame.quit()
