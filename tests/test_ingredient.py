import pytest
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:

    @pytest.mark.parametrize("ingredient_type, name, price, expected_type", [
        (INGREDIENT_TYPE_SAUCE, "Соус фирменный Space Sauce", 80, INGREDIENT_TYPE_SAUCE),
        (INGREDIENT_TYPE_FILLING, "Мини-салат Экзо-Плантаго", 4400, INGREDIENT_TYPE_FILLING),
    ])
    def test_ingredient_get_type(self, ingredient_type, name, price, expected_type):

        # проверка, что метод get_type() возвращает корректный тип ингредиента.
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == expected_type

    @pytest.mark.parametrize("ingredient_type, name, price, expected_name", [
        (INGREDIENT_TYPE_SAUCE, "Соус фирменный Space Sauce", 80, "Соус фирменный Space Sauce"),
        (INGREDIENT_TYPE_FILLING, "Мини-салат Экзо-Плантаго", 4400, "Мини-салат Экзо-Плантаго"),
    ])
    def test_ingredient_get_name(self, ingredient_type, name, price, expected_name):

        # проверка, что метод get_name() возвращает корректное название ингредиента.
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == expected_name

    @pytest.mark.parametrize("ingredient_type, name, price, expected_price", [
        (INGREDIENT_TYPE_SAUCE, "Соус фирменный Space Sauce", 80, 80),
        (INGREDIENT_TYPE_FILLING, "Мини-салат Экзо-Плантаго", 4400, 4400),
    ])
    def test_ingredient_get_price(self, ingredient_type, name, price, expected_price):

        # проверка, что метод get_price() возвращает корректную цену ингредиента.
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == expected_price
