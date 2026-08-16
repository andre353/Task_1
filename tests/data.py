from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


# Данные для параметризации тестов булочки (Bun)
BUN_NAMES = ["Бриошь", "Булочка с кунжутом", "Black Bun"]
BUN_PRICES = [201.50, 100, 0.0]

# Данные для параметризации стоимости класса Burger
# Формат: (цена_булки, цена_ингредиента, ожидаемая_итоговая_цена)
BURGER_PRICE_DATA = [
    (100.0, 50.0, 250.0),    # Стандартный расчет: 100*2 + 50
    (150.50, 75.20, 376.2),  # Расчет с плавающей точкой: 150.5*2 + 75.2
    (0.0, 0.0, 0.0),         # Граничные значения (бесплатный бургер)
    (200.0, 0.0, 400.0),     # Бургер без ингредиентов (только булки)
]

# Данные для параметризации чека класса Burger
# Формат: (имя_булки, цена_булки, тип_ингредиента, имя_ингредиента, цена_ингредиента, общая_цена)
BURGER_RECEIPT_DATA = [
    ("black bun", 100.0, "SAUCE", "chili sauce", 50.0, "250.0"),
    ("white bun", 150.0, "FILLING", "cutlet", 120.0, "420.0")
]

# Данные для параметризации тестов класса Ingredients
INGREDIENT_INIT_DATA = [
    ("SAUCE", "chili sauce", 100.0),
    ("FILLING", "cutlet", 200.50),
    ("FILLING", "dino cutlet", 0.0)
]

INGREDIENT_TYPES = [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING]
INGREDIENT_NAMES = ["chili sauce", "cutlet", "dino cutlet"]
INGREDIENT_PRICES = [100.0, 200.50, 0.0]

EXPECTED_BUNS_COUNT = 3
EXPECTED_INGREDIENTS_COUNT = 6

# Данные первой булки для выборочной проверки
FIRST_BUN_NAME = "black bun"
FIRST_BUN_PRICE = 100

# Данные первого ингредиента для выборочной проверки
FIRST_ING_NAME = "hot sauce"
FIRST_ING_PRICE = 100