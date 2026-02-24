import pytest
from shipping import calculate_shipping, apply_discount, final_price, express_shipping


# ─── calculate_shipping ───────────────────────────────────────────────────────

def test_normal_shipping():
    """5kg parcel, 100km → 250.0"""
    assert calculate_shipping(5, 100) == 250.0

def test_small_parcel():
    assert calculate_shipping(1, 10) == 5.0

def test_zero_weight_raises():
    with pytest.raises(ValueError, match="Weight must be positive"):
        calculate_shipping(0, 100)

def test_negative_weight_raises():
    with pytest.raises(ValueError):
        calculate_shipping(-5, 100)

def test_negative_distance_raises():
    with pytest.raises(ValueError, match="Distance cannot be negative"):
        calculate_shipping(5, -10)

def test_zero_distance():
    """Zero distance (local pickup) = free shipping"""
    assert calculate_shipping(5, 0) == 0.0


# ─── apply_discount ───────────────────────────────────────────────────────────

def test_discount_20_percent():
    assert apply_discount(100, 20) == 80.0

def test_no_discount():
    assert apply_discount(100, 0) == 100.0

def test_full_discount():
    assert apply_discount(100, 100) == 0.0

def test_discount_overflow_raises():
    with pytest.raises(ValueError, match="Discount must be 0-100"):
        apply_discount(100, 150)

def test_negative_discount_raises():
    with pytest.raises(ValueError):
        apply_discount(100, -10)


# ─── final_price ──────────────────────────────────────────────────────────────

def test_final_price_with_discount():
    # 5kg × 100km × 0.5 = 250.0, then 20% off = 200.0
    assert final_price(5, 100, 20) == 200.0

def test_final_price_no_discount():
    assert final_price(5, 100, 0) == 250.0

def test_final_price_full_discount():
    assert final_price(5, 100, 100) == 0.0


# ─── express_shipping ─────────────────────────────────────────────────────────

class TestExpressShipping:

    def test_double_standard_rate(self):
        """5kg × 100km × 0.5 × 2 = 500.0"""
        assert express_shipping(5, 100) == 500.0

    def test_small_parcel(self):
        # standard = 1 × 10 × 0.5 = 5.0  →  express = 10.0
        assert express_shipping(1, 10) == 10.0

    def test_is_exactly_twice_standard(self):
        standard = calculate_shipping(7, 80)
        assert express_shipping(7, 80) == standard * 2

    def test_zero_distance_is_free(self):
        assert express_shipping(5, 0) == 0.0

    def test_zero_weight_raises(self):
        with pytest.raises(ValueError, match="Weight must be positive"):
            express_shipping(0, 100)

    def test_negative_weight_raises(self):
        with pytest.raises(ValueError, match="Weight must be positive"):
            express_shipping(-3, 100)

    def test_negative_distance_raises(self):
        with pytest.raises(ValueError, match="Distance cannot be negative"):
            express_shipping(5, -50)

    def test_return_type_is_float(self):
        assert isinstance(express_shipping(2, 30), float)
