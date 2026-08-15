import pytest
from praktikum.burger import Burger

@pytest.fixture
def burger():
    """Фикстура возвращает объект бургера перед каждым тестом"""
    return Burger()
