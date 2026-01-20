import pygame
from .assets import assets
from .objects.tile import Tile

def run():
    pygame.init()

    size = width, height = 1280 , 720
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    assets.load_all()

    bg_img = assets.grass
    bg_rect = bg_img.get_rect()

    tiles = {(x,y): Tile(bg_img, [x, y]) for x in range(0, size[0], bg_rect.width) for y in range(0, size[1], bg_rect.height)}

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for _pos, tile in tiles.items():
            tile.draw(screen)

        tool.draw(screen, (0, 0))

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
