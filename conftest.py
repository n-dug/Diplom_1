import pytest
import data as d

from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE as SAUCE
from unittest.mock import Mock


@pytest.fixture()
def mock_bun():
    mock_bun = Mock()
    mock_bun.name = d.BurgerExample.BUN_NAME_1
    mock_bun.price = d.BurgerExample.BUN_PRICE_1
    mock_bun.get_name.return_value = d.BurgerExample.BUN_NAME_1
    mock_bun.get_price.return_value = d.BurgerExample.BUN_PRICE_1
    return mock_bun


@pytest.fixture()
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.get_type = SAUCE
    mock_ingredient.get_name = d.BurgerExample.INGREDIENT_NAME_1
    mock_ingredient.get_price = d.BurgerExample.INGREDIENT_PRICE_1
    return mock_ingredient
