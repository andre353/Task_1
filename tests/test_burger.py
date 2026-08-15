import pytest
from unittest.mock import Mock
from tests.data import BURGER_PRICE_DATA, BURGER_RECEIPT_DATA


class TestBurger:

    def test_set_buns(self, burger):
        # Используем мок объекта Bun для независимости теста
        mock_bun = Mock()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger):
        # Используем мок объекта Ingredient для независимости теста
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients

    def test_remove_ingredient(self, burger):
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, burger):
        mock_ing_1 = Mock()
        mock_ing_2 = Mock()
        burger.add_ingredient(mock_ing_1)
        burger.add_ingredient(mock_ing_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_ing_2, mock_ing_1]

    @pytest.mark.parametrize("bun_price, ing_price, expected_total", BURGER_PRICE_DATA)
    def test_get_price_calculates_correctly(self, burger, bun_price, ing_price, expected_total):
        # Создаем моки
        mock_bun = Mock()
        mock_ingredient = Mock()
        
        # Динамически подставляем цены из файла data.py в моки
        mock_bun.get_price.return_value = bun_price
        mock_ingredient.get_price.return_value = ing_price
        
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        
        # Проверяем результирующее метода
        assert burger.get_price() == expected_total

    @pytest.mark.parametrize(
        "bun_name, bun_price, ing_type, ing_name, ing_price, expected_total", 
        BURGER_RECEIPT_DATA
    )
    def test_get_receipt_format(self, burger, bun_name, bun_price, ing_type, ing_name, ing_price, expected_total):
        mock_bun = Mock()
        mock_bun.get_name.return_value = bun_name
        mock_bun.get_price.return_value = bun_price
        
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = ing_type
        mock_ingredient.get_name.return_value = ing_name
        mock_ingredient.get_price.return_value = ing_price
        
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        
        receipt = burger.get_receipt()
        
        # Проверяем форматирование строк с параметризованными данными
        assert f"(==== {bun_name} ====)" in receipt and f"= {ing_type.lower()} {ing_name} =" in receipt and f"Price: {expected_total}" in receipt
