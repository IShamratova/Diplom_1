import sys
import os
import pytest
from unittest.mock import Mock
from bun import Bun
from ingredient import Ingredient

# Добавляем родительскую директорию (корень проекта) в sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture
def bun_mock():
    # Фикстура для мока булки.
    return Mock(spec=Bun)

@pytest.fixture
def ingredient_mock():
    # Фикстура для мока ингредиента.
    return Mock(spec=Ingredient)

