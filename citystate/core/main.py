import pygame

from pygame.locals import *
from citystate.core.utils import (
    load_image,
    load_images,
    load_sound
)
from citystate.data.player import Player
from citystate.data.city import City
from citystate.data.score import Score
from citystate.core.constants import (
    SCREEN_RECT,
    NUMBER_OF_CITIES,
)


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
    win_style = 0  # | FULLSCREEN
    best_depth = pygame.display.mode_ok(SCREEN_RECT.size, win_style, 32)
    screen = pygame.display.set_mode(SCREEN_RECT.size, win_style, best_depth)
    # create the background, tile the bgd image
    bgdtile = load_image('map.gif')
    background = pygame.Surface(SCREEN_RECT.size)
    for x in range(0, SCREEN_RECT.width, bgdtile.get_width()):
        background.blit(bgdtile, (x, 0))
    screen.blit(background, (0, 0))
    pygame.display.flip()

    all_container = pygame.sprite.RenderUpdates()
    # Initialize cities
    city_container = pygame.sprite.Group()
    for i in range(NUMBER_OF_CITIES):
        City([city_container, all_container])

    score = Score(all_container)
    # Initialize player
    player = Player(all_container)
    while player.alive():
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return

        # clear and update sprites
        all_container.clear(screen, background)
        all_container.update()
        # Player moves
        key_states = pygame.key.get_pressed()
        player.move(key_states[K_RIGHT] - key_states[K_LEFT], key_states[K_DOWN] - key_states[K_UP])
        # Detect play & city collision
        for city in pygame.sprite.spritecollide(player, city_container, 1):
            # TODO play sound
            city.kill()
            if city.occupied(player):
                player.occupy_city()
                score.update_score(player.cities_count)
        pygame.display.update(all_container.draw(screen))

    if pygame.mixer:
        pygame.mixer.music.fadeout(1000)
    pygame.time.wait(1000)
    pygame.quit()
