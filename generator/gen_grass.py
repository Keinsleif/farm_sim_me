import random
import pygame


def create_pixel_art():
    pygame.init()
    
    grass_size = (32, 32)
    grass_surface = pygame.Surface(grass_size)
    
    for x in range(0, grass_size[0], 2):
        for y in range(0, grass_size[1], 2):
            base_green = 100
            variation = random.randint(-20, 20)
            g = max(0, min(255, base_green + variation))
            r = max(0, min(255, 30 + random.randint(-10, 10)))
            b = max(0, min(255, 30 + random.randint(-10, 10)))
            
            grass_surface.set_at((x, y), (r, g, b))
            grass_surface.set_at((x + 1, y), (r, g, b))
            grass_surface.set_at((x, y + 1), (r, g, b))
            grass_surface.set_at((x + 1, y + 1), (r, g, b))

    pygame.draw.rect(grass_surface, (50, 80, 50), (0,0,32,32), 1)

    pygame.image.save(grass_surface, "grass.png")

if __name__ == '__main__':
    create_pixel_art()