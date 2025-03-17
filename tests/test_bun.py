import pytest
from bun import Bun


class TestBun:

    @pytest.mark.parametrize("name, price, expected_name", [
        ("Флюоресцентная булка R2-D3", 988, "Флюоресцентная булка R2-D3"),
        ("Краторная булка N-200i", 1255, "Краторная булка N-200i"),
    ])
    def test_bun_get_name(self, name, price, expected_name):

        # проверка, что метод get_name() возвращает корректное имя булки.
        bun = Bun(name, price)
        assert bun.get_name() == expected_name

    @pytest.mark.parametrize("name, price, expected_price", [
        ("Флюоресцентная булка R2-D3", 988, 988),
        ("Краторная булка N-200i", 1255, 1255),
    ])
    def test_bun_get_price(self, name, price, expected_price):

        # проверка, что метод get_price() возвращает корректную цену булки.
        bun = Bun(name, price)
        assert bun.get_price() == expected_price
