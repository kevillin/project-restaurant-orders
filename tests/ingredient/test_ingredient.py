from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient = Ingredient("farinha")
    ingredient2 = Ingredient("queijo parmesão")

    assert ingredient.__hash__() == "farinha"
    assert ingredient.__hash__() != "finha"
    assert ingredient.__repr__() == "Ingredient('farinha')"
    assert ingredient.__repr__() != "Ingreient('farnha')"

    assert ingredient != ingredient2
