from pygame import Surface
from farm_sim_me.assets import assets


class ResourceStorage:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ResourceStorage, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        
        self._initialized = True

        self.money = -5000  # 所持金

        self.day = 1
        self.max_stamina = 100
        self.current_stamina = 100

        self.inventory = {
            "seed_wheat": 10,  # 小麦の種
            "wheat": 0         # 収穫した小麦
        }

    def update(self, dt: int):
        pass

    def draw(self, screen: Surface, pos):
        stats_str = f"日数：{self.day}日"
        stats_str += f"\n金：{self.money}"
        stats_str += f"\nスタミナ：{self.current_stamina}/{self.max_stamina}"
        stats_str += f"\n小麦の種：{self.inventory["seed_wheat"]}"
        stats_str += f"\n小麦：{self.inventory["wheat"]}"
        text = assets.font_title.render(stats_str, True, (255,255,255))
        screen.blit(text, pos)

    def use_stamina(self, amount):
        """
        スタミナを消費する
        戻り値: 消費に成功したらTrue, 足りなければFalse
        """
        if self.current_stamina >= amount:
            self.current_stamina -= amount
            print(f"Stamina used: -{amount}. Current: {self.current_stamina}/{self.max_stamina}")
            return True
        else:
            print("Not enough stamina!")
            return False

    def upgrade_stamina(self) -> bool:
        """
        小麦を消費してスタミナの最大値を上昇させる
        """
        if self.inventory.get("wheat", 0) >= 10:
            self.inventory["wheat"] -= 10
            self.max_stamina += 10

    def next_day(self):
        """一日を進める"""
        self.day += 1
        self.current_stamina = self.max_stamina
        print(f"--- Day {self.day} Started ---")

    def has_seed(self, crop_type):
        """指定した作物の種を持っているか確認"""
        key = f"seed_{crop_type}"
        return self.inventory.get(key, 0) > 0

    def consume_seed(self, crop_type):
        """種を1つ消費する。成功したらTrueを返す"""
        key = f"seed_{crop_type}"
        if self.has_seed(crop_type):
            self.inventory[key] -= 1
            print(f"Consumed {key}. Remaining: {self.inventory[key]}")
            return True
        return False

    def add_harvest(self, crop_type, amount=1):
        """収穫物をインベントリに追加する"""

        current = self.inventory.get(crop_type, 0)
        self.inventory[crop_type] = current + amount
        print(f"Harvested {crop_type}! Total: {self.inventory[crop_type]}")

    def sell_crop(self, crop_type):
        """収穫物を売ってお金にする"""
        count = self.inventory.get(crop_type, 0)
        if count > 0:

            prices = {"wheat": 30}
            price = prices.get(crop_type, 0)
            
            earn = price * count
            self.money += earn
            self.inventory[crop_type] = 0
            print(f"Sold {count} {crop_type} for {earn}G. Current Money: {self.money}G")
            return earn
        return 0

    def buy_seed(self, crop_type, amount = 10):
        prices = {"seed_wheat": 10}
        price = prices.get(f"seed_{crop_type}", 0)

        resource_storage.money -= price * amount
        self.inventory[f"seed_{crop_type}"] += amount
        print(f"Buy {amount} seed_{crop_type} for {price * amount}G. Current Money: {self.money}G")
        return amount

resource_storage = ResourceStorage()