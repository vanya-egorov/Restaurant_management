# import json
# from dataclasses import dataclass
#
#
# @dataclass
# class Dish:
#     name: str
#     price: str
#
#     def convertor(self):
#         return json.dumps({
#             "name": self.name,
#             "price": self.price
#         })
#
#     @classmethod
#     def from_str(cls, raw_dish: str) -> 'Dish':
#         dish_dict = json.loads(raw_dish)
#         return Dish(
#             name=dish_dict["name"],
#             price=dish_dict["price"]
#         )