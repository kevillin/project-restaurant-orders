from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    dish = Dish("Pizza", 15.99)
    dish2 = Dish("Macarronada", 14.99)
    ingredient = Ingredient("ovos")
    ingredient.restrictions = {Restriction.GLUTEN}
    # restrictions = dish.get_restrictions()
    amount = 3

    dish.add_ingredient_dependency(ingredient, amount)
    assert dish.get_ingredients() == {ingredient}
    assert "batata" not in dish.get_ingredients()
    assert dish.recipe[ingredient] == amount
    assert hash(dish) != hash(dish2)
    assert hash(dish) == hash(Dish("Pizza", 15.99))
    assert dish.__repr__() == "Dish('Pizza', R$15.99)"
    assert dish.__repr__() != "Ingreient('farnha')"
    assert dish != dish2
    assert dish == Dish("Pizza", 15.99)
    assert dish.get_restrictions() == {Restriction.GLUTEN}

    assert dish.name != "Batata"
    assert dish.name == "Pizza"

    with pytest.raises(TypeError):
        dish = Dish("Dish price must be float.", "15.99")

    with pytest.raises(ValueError):
        dish = Dish("Dish price must be greater then zero.", -15.99)
