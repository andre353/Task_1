import pytest
from praktikum.bun import Bun
from tests.data import BUN_NAMES, BUN_PRICES


# Базовые значения для тестов, где этот параметр не является целевым
DEFAULT_NAME = "Дефолтная булка"
DEFAULT_PRICE = 150.0


class TestBun:

    # Тестируем независимость инициализации (правильно ли записываются атрибуты)
    @pytest.mark.parametrize("name", BUN_NAMES)
    @pytest.mark.parametrize("price", BUN_PRICES)
    def test_bun_init_sets_correct_attributes(self, name, price):
        bun = Bun(name, price)
        assert bun.name == name and bun.price == price

    # Тестируем метод get_name() отдельно
    @pytest.mark.parametrize("name", BUN_NAMES)
    def test_bun_get_name_returns_correct_value(self, name):
        bun = Bun(name, DEFAULT_PRICE) # цена тут не важна для теста имени
        assert bun.get_name() == name

    # Тестируем метод get_price() отдельно
    @pytest.mark.parametrize("price", BUN_PRICES)
    def test_bun_get_price_returns_correct_value(self, price):
        bun = Bun(DEFAULT_NAME, price) # имя тут не важно для теста цены
        assert bun.get_price() == price
