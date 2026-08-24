import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE 
from data import INGREDIENT_INIT_DATA, INGREDIENT_TYPES, INGREDIENT_NAMES, INGREDIENT_PRICES, DEFAULT_NAME, DEFAULT_PRICE


class TestIngredient:

    # Тестируем независимость инициализации
    @pytest.mark.parametrize("ingredient_type,name,price", INGREDIENT_INIT_DATA)
    def test_ingredient_init_sets_correct_attributes(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.type == ingredient_type and ingredient.name == name and ingredient.price == price

    @pytest.mark.parametrize("ingredient_type", INGREDIENT_TYPES)
    def test_ingredient_get_type_returns_correct_value(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, DEFAULT_NAME, DEFAULT_PRICE)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize("name", INGREDIENT_NAMES)
    def test_ingredient_get_name_returns_correct_value(self, name):
        DEFAULT_TYPE = INGREDIENT_TYPE_SAUCE
        ingredient = Ingredient(DEFAULT_TYPE, name, DEFAULT_PRICE)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("price", INGREDIENT_PRICES)
    def test_ingredient_get_price_returns_correct_value(self, price):
        DEFAULT_TYPE = INGREDIENT_TYPE_SAUCE
        ingredient = Ingredient(DEFAULT_TYPE, DEFAULT_NAME, price)
        assert ingredient.get_price() == price
