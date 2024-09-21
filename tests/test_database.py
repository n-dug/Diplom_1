from praktikum.database import Database


class TestDatabase:

    def test_available_buns_success(self):
        data = Database()
        buns = data.available_buns()
        assert buns[0].name == 'black bun'

    def test_available_ingredients_success(self):
        data = Database()
        ingredients = data.available_ingredients()
        assert ingredients[0].name == 'hot sauce'
