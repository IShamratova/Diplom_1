import pytest
from database import Database
from bun import Bun
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE


class TestDatabase:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.database = Database()

    # Тесты для available_ingredients()

    def test_available_buns_count(self):
        # проверка, что available_buns() возвращает 3 булки.
        buns = self.database.available_buns()
        assert len(buns) == 3

    def test_available_buns_instance(self):
        # проверка, что available_buns() возвращает объекты типа Bun.
        buns = self.database.available_buns()
        assert all(isinstance(bun, Bun) for bun in buns)

    def test_available_buns_first_name(self):
        # проверка, что первая булка называется 'black bun'.
        buns = self.database.available_buns()
        assert buns[0].get_name() == "black bun"

    def test_available_buns_first_price(self):
        # проверка, что цена первой булки равна 100.
        buns = self.database.available_buns()
        assert buns[0].get_price() == 100

    # Тесты для available_ingredients()

    def test_available_ingredients_count(self):
        # проверка, что available_ingredients() возвращает 6 ингредиентов."""
        ingredients = self.database.available_ingredients()
        assert len(ingredients) == 6

    def test_available_ingredients_instance(self):
        # проверкат, что available_ingredients() возвращает объекты типа Ingredient."""
        ingredients = self.database.available_ingredients()
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)

    def test_available_ingredients_first_type(self):
        # проверка, что первый ингредиент имеет тип INGREDIENT_TYPE_SAUCE."""
        ingredients = self.database.available_ingredients()
        assert ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE

    def test_available_ingredients_first_name(self):
        # проверка, что первый ингредиент называется 'hot sauce'."""
        ingredients = self.database.available_ingredients()
        assert ingredients[0].get_name() == "hot sauce"

    def test_available_ingredients_first_price(self):
        # проверка, что цена первого ингредиента равна 100."""
        ingredients = self.database.available_ingredients()
        assert ingredients[0].get_price() == 100

