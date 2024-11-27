import data as d

from unittest.mock import Mock
from praktikum.burger import Ingredient
from praktikum.burger import Burger
from praktikum.burger import Bun
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE as SAUCE
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING as FILLING


class TestBurger:

    def test_set_buns_success(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert (burger.bun.get_name() == d.BurgerExample.BUN_NAME_1
                and burger.bun.get_price() == d.BurgerExample.BUN_PRICE_1)

    def test_add_ingredient_success(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]

    def test_remove_ingredient_success(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient_success(self):
        burger = Burger()
        ingredient_0 = Ingredient(SAUCE, d.BurgerExample.INGREDIENT_NAME_1, d.BurgerExample.INGREDIENT_PRICE_1)
        ingredient_1 = Ingredient(FILLING, d.BurgerExample.INGREDIENT_NAME_2, d.BurgerExample.INGREDIENT_PRICE_2)
        burger.add_ingredient(ingredient_0)
        burger.add_ingredient(ingredient_1)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingredient_1, ingredient_0]

    def test_get_price_success(self, mock_bun, mock_ingredient):
        burger = Burger()
        mock_bun.get_price.return_value = 50
        burger.set_buns(mock_bun)
        mock_ingredient.get_type = Mock(return_value="filling")
        mock_ingredient.get_name = Mock(return_value="Ingredient Name")
        mock_ingredient.get_price = Mock(return_value=100)
        burger.add_ingredient(mock_ingredient)
        expected_price = 50 * 2 + 100
        assert burger.get_price() == expected_price

    def test_get_receipt_success(self):
        bun = Mock(spec=Bun)
        bun.get_name.return_value = "Sesame Bun"
        bun.get_price.return_value = 20
        ingredient = Mock(spec=Ingredient)
        ingredient.get_name.return_value = "Lettuce"
        ingredient.get_type.return_value = "Filling"
        ingredient.get_price.return_value = 10
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        expected_receipt = (
            "(==== Sesame Bun ====)\n"
            "= filling Lettuce =\n"
            "(==== Sesame Bun ====)\n\n"
            "Price: 50"
        )
        assert burger.get_receipt() == expected_receipt
