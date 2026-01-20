import pygame

from farm_sim_me.shared import ToolTypes

from .objects.farmland import FarmLand
from .assets import assets
from .objects.tile import Tile

TILE_SIZE = 32
FARM_WIDTH = 20
FARM_HEIGHT = 10

def run():
    pygame.init()

    size = width, height = (1280 , 720)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    assets.load_all()

    bg_img = assets.grass
    bg_rect = bg_img.get_rect()

    farmrect = (((size[0] - TILE_SIZE * FARM_WIDTH) / 2, (size[1] - TILE_SIZE * FARM_HEIGHT) /2), ((size[0] + TILE_SIZE * FARM_WIDTH) / 2, (size[1] + TILE_SIZE * FARM_HEIGHT) / 2))
    tiles = []
    farmlands: dict[tuple[float, float], FarmLand] = {}
    for x in range(0, size[0], bg_rect.width):
        for y in range(0, size[1], bg_rect.height):
            if x >= farmrect[0][0] and x < farmrect[1][0] and y >= farmrect[0][1] and y <= farmrect[1][1]:
                farmlands[(x,y)] = FarmLand((x,y))
            else:
                if x == 0 and y == 0:
                    tiles.append(Tile(assets.blank, (x, y)))
                    continue
                tiles.append(Tile(assets.grass, (x,y)))

    running = True
    tool = ToolTypes.HOE
    mousedownTileStartPos = None
    mousedownTileEndPos = None
    while running:
        for tile in tiles:
            tile.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for pos, tile in farmlands.items():
                        if event.pos[0] >= pos[0] and event.pos[0] < pos[0] + TILE_SIZE and event.pos[1] >= pos[1] and event.pos[1] < pos[1] + TILE_SIZE:
                            mousedownTileStartPos = pos
                elif event.button == 3:
                    tool = tool.next_tool()
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if mousedownTileStartPos is not None:
                    for pos, tile in farmlands.items():
                        if pos[0] >= mousedownTileStartPos[0] and pos[0] < event.pos[0] and pos[1] >= mousedownTileStartPos[1] and pos[1] < event.pos[1]:
                            tile.action(tool)
                    mousedownTileStartPos = None
                    mousedownTileEndPos = None
            elif event.type == pygame.MOUSEMOTION and mousedownTileStartPos is not None:
                mousedownTileEndPos = [TILE_SIZE * ((event.pos[0] // TILE_SIZE) + 1), TILE_SIZE * ((event.pos[1] // TILE_SIZE) + 1)]

        for _pos, tile in farmlands.items():
            tile.update()

        for _pos, tile in farmlands.items():
            tile.draw(screen)

        tool.draw(screen, (0, 0))

        if mousedownTileEndPos is not None and mousedownTileStartPos is not None:
            pygame.draw.rect(screen, (64, 160, 200), (mousedownTileStartPos[0], mousedownTileStartPos[1], mousedownTileEndPos[0] - mousedownTileStartPos[0], mousedownTileEndPos[1] - mousedownTileStartPos[1]), 2)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
