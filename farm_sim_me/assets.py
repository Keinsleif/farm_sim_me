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
        
        self.blank = None
        self.grass = None
        self.tilled = None
        self.hydrated = None
        self.crop1 = None
        self.crop2 = None
        self.crop3 = None

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
        self.blank = pygame.Surface((32,32))
        self.grass = self._load_single("grass.png")
        self.tilled = self._load_single("tilled.png")
        self.hydrated = self._load_single("hydrated.png")
        self.crop1 = self._load_single("crop-1.png")
        self.crop2 = self._load_single("crop-2.png")
        self.crop3 = self._load_single("crop-3.png")

assets = AssetManager()