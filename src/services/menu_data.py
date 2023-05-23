import csv
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.data(source_path)

    def data(self, source_path) -> None:
        with open(source_path, 'r') as file:
            archive = csv.reader(file)
            next(archive)

            for a in archive:
                dish_name = a[0]
                dish_price = float(a[1])
                ingredient_name = a[2]
                ingredient_quantity = float(a[3])

                dish = self.generate_dish(dish_name, dish_price)
                ingredient = Ingredient(ingredient_name)
                dish.add_ingredient_dependency(ingredient, ingredient_quantity)

    def generate_dish(self, name, price):
        for dish in self.dishes:
            if dish.name == name:
                return dish

        new_dish = Dish(name, price)
        self.dishes.add(new_dish)
        return new_dish
