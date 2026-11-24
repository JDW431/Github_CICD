import pytest

from orderlab.pricing import subtotal
from orderlab.pricing import finaltotal


def test_subtotal_normal():
    assert subtotal(10000, 2) == 20000

def test_subtotal_zero():
    assert subtotal(0, 3) == 0

def test_subtotal_negative():
    with pytest.raises(ValueError):
        subtotal(-100, 2)


def test_finaltotal_T1():
    assert finaltotal(49999, 1, 0) == 52999

def test_finaltotal_T2():
    assert finaltotal(50000, 1, 0) == 50000

def test_finaltotal_T3():
    assert finaltotal(50001, 1, 0) == 50001

def test_discount_below_zero():
    with pytest.raises(ValueError,):
        finaltotal(10000, 2, -1)

def test_discount_over_100():
    with pytest.raises(ValueError, match="invalid discount"):
        finaltotal(10_000, 2, 101)
