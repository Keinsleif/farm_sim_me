import random
import pygame


def create_soil_assets():
    pygame.init()
    
    tile_size = (32, 32)
    
    land_surface = pygame.Surface(tile_size)
    
    for y in range(0, tile_size[1], 2):
        for x in range(0, tile_size[0], 2):
            # ベースカラー（明るい茶色）
            base_r, base_g, base_b = 160, 110, 60
            
            # 表面のざらつき（ノイズ）
            offset = random.randint(-15, 15)
            
            r = max(0, min(255, base_r + offset))
            g = max(0, min(255, base_g + offset))
            b = max(0, min(255, base_b + offset))
            
            land_surface.set_at((x, y), (r, g, b))
            land_surface.set_at((x + 1, y), (r, g, b))
            land_surface.set_at((x, y + 1), (r, g, b))
            land_surface.set_at((x + 1, y + 1), (r, g, b))

    pygame.draw.rect(land_surface, (base_r, base_g, base_b), (0,0,32,32), 2)

    pygame.image.save(land_surface, "land.png")

    # ==========================================
    # 1. 耕された土（乾燥） - Dry Tilled Soil
    # ==========================================
    dry_surface = pygame.Surface(tile_size)
    
    for y in range(0, tile_size[1], 2):
        for x in range(0, tile_size[0], 2):
            # ベースカラー（明るい茶色）
            base_r, base_g, base_b = 160, 110, 60
            
            if y % 8 == 6:
                offset = -40 # 影を落とす
            else:
                # 表面のざらつき（ノイズ）
                offset = random.randint(-15, 15)
            
            r = max(0, min(255, base_r + offset))
            g = max(0, min(255, base_g + offset))
            b = max(0, min(255, base_b + offset))
            
            dry_surface.set_at((x, y), (r, g, b))
            dry_surface.set_at((x + 1, y), (r, g, b))
            dry_surface.set_at((x, y + 1), (r, g, b))
            dry_surface.set_at((x + 1, y + 1), (r, g, b))

    pygame.draw.rect(dry_surface, (base_r, base_g, base_b), (0,0,32,32), 2)

    pygame.image.save(dry_surface, "tilled.png")

    # ==========================================
    # 2. 耕された土（濡れ） - Wet Tilled Soil
    # ==========================================
    wet_surface = pygame.Surface(tile_size)
    
    for y in range(0, tile_size[1],  2):
        for x in range(0, tile_size[0], 2):
            # ベースカラー（水を含んで暗くなった濃い茶色）
            base_r, base_g, base_b = 90, 60, 40
            
            # 濡れている時も畝の影は必要
            if y % 8 == 6:
                offset = -30
            else:
                # 濡れていると色は少し均一になり、ノイズは控えめになる傾向がある
                offset = random.randint(-8, 8)
            
            r = max(0, min(255, base_r + offset))
            g = max(0, min(255, base_g + offset))
            b = max(0, min(255, base_b + offset))
            
            wet_surface.set_at((x, y), (r, g, b))
            wet_surface.set_at((x + 1, y), (r, g, b))
            wet_surface.set_at((x, y + 1), (r, g, b))
            wet_surface.set_at((x + 1, y + 1), (r, g, b))

    pygame.draw.rect(wet_surface, (base_r, base_g, base_b), (0,0,32,32), 2)

    pygame.image.save(wet_surface, "hydrated.png")

if __name__ == '__main__':
    create_soil_assets()