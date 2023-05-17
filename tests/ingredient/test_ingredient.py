from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient = Ingredient("farinha")
    ingredient2 = Ingredient("queijo parmesão")
    expected_restrictions = {Restriction.GLUTEN}

    assert ingredient.name == "farinha"
    assert ingredient.name != "finha"
    assert ingredient == Ingredient("farinha")
    assert ingredient != Ingredient("queijo parmesão")
    assert hash(ingredient) == hash(Ingredient("farinha"))
    assert ingredient.__repr__() == "Ingredient('farinha')"
    assert ingredient.__repr__() != "Ingreient('farnha')"

    assert ingredient != ingredient2
    assert ingredient.__repr__() != ingredient2.__repr__()
    assert ingredient.__hash__() != ingredient2.__hash__()

    assert ingredient.restrictions == expected_restrictions
