import pygame

from farm_sim_me.objects.store import BuyStaminaTile, BuyStoreTile, SellStoreTile, SleepTile
from farm_sim_me.resource import resource_storage
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
    pygame.display.set_caption("農業で借金返済　目標: 貯蓄10万G")
    clock = pygame.time.Clock()
    assets.load_all()

    bg_img = assets.grass
    bg_rect = bg_img.get_rect()

    farmrect = (((size[0] - TILE_SIZE * FARM_WIDTH) / 2, (size[1] - TILE_SIZE * FARM_HEIGHT) /2), ((size[0] + TILE_SIZE * FARM_WIDTH) / 2, (size[1] + TILE_SIZE * FARM_HEIGHT) / 2))
    tiles: dict[tuple[float, float], FarmLand] = {}
    for x in range(0, size[0], bg_rect.width):
        for y in range(0, size[1], bg_rect.height):
                if x >= farmrect[0][0] and x < farmrect[1][0] and y >= farmrect[0][1] and y <= farmrect[1][1]:
                    tiles[(x,y)] = FarmLand((x,y))
                elif x == ((size[0] - 1) // TILE_SIZE) * TILE_SIZE and y == 0:
                    tiles[(x,y)] = Tile(assets.blank, (x, y))
                elif x == ((size[0] - 1) // TILE_SIZE) * TILE_SIZE and y == 3 * TILE_SIZE:
                    tiles[(x,y)] = SellStoreTile((x, y))
                elif x == ((size[0] - 1) // TILE_SIZE) * TILE_SIZE and y == 4 * TILE_SIZE:
                    tiles[(x,y)] = BuyStoreTile((x, y))
                elif x == ((size[0] - 1) // TILE_SIZE) * TILE_SIZE and y == 5 * TILE_SIZE:
                    tiles[(x,y)] = BuyStaminaTile((x, y))
                elif x == ((size[0] - 1) // TILE_SIZE) * TILE_SIZE and y == 6 * TILE_SIZE:
                    tiles[(x,y)] = SleepTile((x, y))
                else:
                    tiles[(x,y)] = Tile(assets.grass, (x,y))

    running = True
    tool = ToolTypes.HOE
    tool_tooltip = assets.font_desc.render("右クリックでツール切り替え ", True, (255, 255, 255))
    clear_text = assets.font_title.render(f"GAME CLEAR!\n\nかかった日数: {resource_storage.day}", True, (0, 0, 0))
    phase = "normal"
    mousedownTileStartPos = None
    mousedownTileEndPos = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for pos, tile in tiles.items():
                        if event.pos[0] >= pos[0] and event.pos[0] < pos[0] + TILE_SIZE and event.pos[1] >= pos[1] and event.pos[1] < pos[1] + TILE_SIZE:
                            mousedownTileStartPos = pos
                elif event.button == 3:
                    tool = tool.next_tool()
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if mousedownTileStartPos is not None:
                    for pos, tile in tiles.items():
                        if pos[0] >= mousedownTileStartPos[0] and pos[0] < event.pos[0] and pos[1] >= mousedownTileStartPos[1] and pos[1] < event.pos[1]:
                            tile.action(tool)
                    mousedownTileStartPos = None
                    mousedownTileEndPos = None
            elif event.type == pygame.MOUSEMOTION and mousedownTileStartPos is not None:
                mousedownTileEndPos = [TILE_SIZE * ((event.pos[0] // TILE_SIZE) + 1), TILE_SIZE * ((event.pos[1] // TILE_SIZE) + 1)]

        for _pos, tile in tiles.items():
            tile.update(clock.get_time())

        resource_storage.update(clock.get_time())

        if resource_storage.money > 100000:
            phase = "end"

        if phase == "end":
            screen.fill((255,255,255))
            text_rect = clear_text.get_rect(center = (size[0] / 2, size[1] / 2))
            screen.blit(clear_text, text_rect)
        else:
            for _pos, tile in tiles.items():
                tile.draw(screen)

            tool.draw(screen, (((size[0] - 1) // TILE_SIZE) * TILE_SIZE, 0))
            screen.blit(tool_tooltip, tool_tooltip.get_rect(topright = (((size[0] - 1) // TILE_SIZE) * TILE_SIZE, 0)))
            resource_storage.draw(screen, (0, 0))

            if mousedownTileEndPos is not None and mousedownTileStartPos is not None:
                pygame.draw.rect(screen, (64, 160, 200), (mousedownTileStartPos[0], mousedownTileStartPos[1], mousedownTileEndPos[0] - mousedownTileStartPos[0], mousedownTileEndPos[1] - mousedownTileStartPos[1]), 2)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
