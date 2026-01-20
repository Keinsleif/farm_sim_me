from enum import Enum

from farm_sim_me.assets import assets

class ToolTypes(Enum):
    HOE = 0
    WATERING = 1
    SEED = 2
    HARVEST = 3

    def next_tool(self):
        return ToolTypes((self.value + 1) % 4)

    def draw(self, screen, pos):
        image = None

        if self == self.HOE:
            image = assets.hoe
        elif self == self.WATERING:
            image = assets.watering
        elif self == self.SEED:
            image = assets.seed
        elif self == self.HARVEST:
            image = assets.scythe

        if image is not None:
            screen.blit(image, pos)
