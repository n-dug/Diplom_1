import data as d
import pytest
from praktikum.bun import Bun



class TestBun:

    @pytest.mark.parametrize('name,price', [
        (d.BurgerExample.BUN_NAME_1, d.BurgerExample.BUN_PRICE_1),
        (d.BurgerExample.BUN_NAME_2, d.BurgerExample.BUN_PRICE_2)
    ])
    def test_get_name_success(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize('name,price', [
        (d.BurgerExample.BUN_NAME_1, d.BurgerExample.BUN_PRICE_1),
        (d.BurgerExample.BUN_NAME_2, d.BurgerExample.BUN_PRICE_2)
    ])
    def test_get_price_success(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
