import pytest
from tests.data import (
    EXPECTED_BUNS_COUNT,
    EXPECTED_INGREDIENTS_COUNT,
    FIRST_BUN_NAME,
    FIRST_BUN_PRICE,
    FIRST_ING_NAME,
    FIRST_ING_PRICE
)


class TestDatabase:

    def test_available_buns_returns_correct_count(self, db):
        buns = db.available_buns()
        assert len(buns) == EXPECTED_BUNS_COUNT

    def test_available_buns_contains_correct_data(self, db):
        first_bun = db.available_buns()
        # available_buns возвращает список объектов класса Bun, под индексом [0] находится первый объект
        assert first_bun[0].get_name() == FIRST_BUN_NAME and first_bun[0].get_price() == FIRST_BUN_PRICE

    def test_available_ingredients_returns_correct_count(self, db):
        ingredients = db.available_ingredients()
        assert len(ingredients) == EXPECTED_INGREDIENTS_COUNT

    def test_available_ingredients_contains_correct_data(self, db):
        first_ingredient = db.available_ingredients()
        assert first_ingredient[0].get_name() == FIRST_ING_NAME and first_ingredient[0].get_price() == FIRST_ING_PRICE
