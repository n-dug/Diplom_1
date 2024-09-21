import data as d

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE as SAUCE


class TestIngredient:

    def test_get_price_success(self):
        ingredient = Ingredient(SAUCE,
                                d.BurgerExample.INGREDIENT_NAME_1,
                                d.BurgerExample.INGREDIENT_PRICE_1)
        assert ingredient.get_price() == d.BurgerExample.INGREDIENT_PRICE_1

    def test_get_name_success(self):
        ingredient = Ingredient(SAUCE,
                                d.BurgerExample.INGREDIENT_NAME_1,
                                d.BurgerExample.INGREDIENT_PRICE_1)
        assert ingredient.get_name() == d.BurgerExample.INGREDIENT_NAME_1

    def test_get_type_success(self):
        ingredient = Ingredient(SAUCE,
                                d.BurgerExample.INGREDIENT_NAME_1,
                                d.BurgerExample.INGREDIENT_PRICE_1)
        assert ingredient.get_type() == SAUCE
