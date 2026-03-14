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

def test_express_normal():
    """5kg, 100km → standard=250.0, express=500.0"""
    assert express_shipping(5, 100) == 500.0

def test_express_is_double_standard():
    """Express must always be exactly 2× the standard rate."""
    assert express_shipping(3, 50) == calculate_shipping(3, 50) * 2

def test_express_zero_distance():
    """Zero distance → free express shipping too."""
    assert express_shipping(5, 0) == 0.0

def test_express_invalid_weight_raises():
    """Inherits validation — zero weight should raise ValueError."""
    with pytest.raises(ValueError, match="Weight must be positive"):
        express_shipping(0, 100)
