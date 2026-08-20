import pytest
from praktikum.burger import Burger
from praktikum.database import Database


@pytest.fixture
def burger():
    """Фикстура возвращает объект бургера перед каждым тестом"""
    return Burger()

@pytest.fixture
def db():
    """Фикстура для создания объекта базы данных перед каждым тестом"""
    return Database()