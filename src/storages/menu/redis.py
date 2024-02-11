from redis import Redis

from src.storages.menu.entities import Dish


class Menu:
    redis: Redis

    def __init__(self, redis: Redis):
        self.redis = redis

    def add_dish(self, dish: Dish):
        self.redis.set(dish.name, dish.convertor())
        self.redis.lpush("menu_dishes", dish.name)

    def get_dish(self, dish_name: str) -> Dish:
        raw_dish = self.redis.get(dish_name)
        return Dish.from_str(raw_dish)

    def change_dish(self, dish: Dish):
        self.redis.set(dish.name, dish.convertor())

    def delete_dish(self, dish: Dish):
        self.redis.delete(dish.name)

    def get_all_menu(self) -> list[Dish]:
        name_menu = self.redis.ltrim("menu_dishes", 0, -1)
        menu_list = []
        for dish_name in name_menu:
            dish = self.get_dish(dish_name)
            menu_list.append(dish)

        return menu_list
