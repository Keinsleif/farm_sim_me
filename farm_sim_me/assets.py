import os
import sys
import pygame


class AssetManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AssetManager, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        
        self.font_title = None
        self.font_desc = None
        
        self.blank = None
        self.grass = None
        self.land = None
        self.tilled = None
        self.hydrated = None
        self.crop1 = None
        self.crop2 = None
        self.crop3 = None

        self.hoe = None
        self.watering = None
        self.seed = None
        self.scythe = None

        self.store_sell = None
        self.store_buy = None
        self.upgrade_stamina = None
        self.sleep = None

        self._initialized = True;

    def get_resource_path(self, filename):
        if getattr(sys, 'frozen', False):
            base_dir = os.path.dirname(sys.executable)
        else:
            base_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(base_dir, "assets",filename)

    def _load_single(self, filename, use_alpha=True):
        path = self.get_resource_path(filename)
        try:
            img = pygame.image.load(path)
            if use_alpha:
                img = img.convert_alpha()
            else:
                img = img.convert()
            return img
        except FileNotFoundError:
            print(f"Error: Cannot find file {path}")
            s = pygame.Surface((32, 32))
            s.fill((255, 0, 255))
            return s
        except pygame.error as e:
            print(f"Pygame Error loading {path}: {e}")
            return pygame.Surface((32, 32))

    def load_all(self):
        self.font_title = pygame.font.Font(self.get_resource_path("NotoSansJP-Bold.ttf"), 24)
        self.font_desc = pygame.font.Font(self.get_resource_path("NotoSansJP-Regular.ttf"), 18)

        self.blank = pygame.Surface((32,32))
        self.blank.fill((255,255,255))
        self.grass = self._load_single("grass.png")
        self.land = self._load_single("land.png")
        self.tilled = self._load_single("tilled.png")
        self.hydrated = self._load_single("hydrated.png")
        self.crop1 = self._load_single("crop-1.png")
        self.crop2 = self._load_single("crop-2.png")
        self.crop3 = self._load_single("crop-3.png")
        self.hoe = self._load_single("tools/hoe.png")
        self.watering = self._load_single("tools/watering.png")
        self.seed = self._load_single("tools/seed.png")
        self.scythe = self._load_single("tools/scythe.png")
        self.store_buy = self._load_single("store_buy.png")
        self.store_sell = self._load_single("store_sell.png")
        self.upgrade_stamina = self._load_single("upgrade_stamina.png")
        self.sleep = self._load_single("sleep.png")

assets = AssetManager()