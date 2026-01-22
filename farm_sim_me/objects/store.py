from farm_sim_me.objects.tile import Tile
from pygame.typing import RectLike

from farm_sim_me.resource import resource_storage
from farm_sim_me.resource import resource_storage
from ..assets import assets

class SellStoreTile(Tile):
    def __init__(self, pos: RectLike):
        self.text = assets.font_desc.render("小麦をすべて売却→", True, (255, 255, 255))
        super().__init__(assets.grass, pos)

    def draw(self, screen):
        super().draw(screen)
        screen.blit(assets.store_sell, self._pos)
        screen.blit(self.text, self.text.get_rect(topright=self._pos))

    def action(self, tool):
        resource_storage.sell_crop("wheat")


class BuyStoreTile(Tile):
    def __init__(self, pos: RectLike):
        self.text = assets.font_desc.render("小麦の種x10を購入→", True, (255, 255, 255))
        super().__init__(assets.grass, pos)

    def draw(self, screen):
        super().draw(screen)
        screen.blit(assets.store_buy, self._pos)
        screen.blit(self.text, self.text.get_rect(topright=self._pos))

    def action(self, tool):
        resource_storage.buy_seed("wheat")

class BuyStaminaTile(Tile):
    def __init__(self, pos: RectLike):
        self.text = assets.font_desc.render("小麦x10で最大スタミナx10増加→", True, (255, 255, 255))
        super().__init__(assets.grass, pos)

    def draw(self, screen):
        super().draw(screen)
        screen.blit(assets.upgrade_stamina, self._pos)
        screen.blit(self.text, self.text.get_rect(topright=self._pos))

    def action(self, tool):
        resource_storage.upgrade_stamina()

class SleepTile(Tile):
    def __init__(self, pos: RectLike):
        self.text = assets.font_desc.render("寝てスタミナを回復→", True, (255, 255, 255))
        super().__init__(assets.grass, pos)

    def draw(self, screen):
        super().draw(screen)
        screen.blit(assets.sleep, self._pos)
        screen.blit(self.text, self.text.get_rect(topright=self._pos))

    def action(self, tool):
        resource_storage.next_day()