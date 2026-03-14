def calculate_shipping(weight: float, distance: float) -> float:
    """
    Calculate shipping cost based on weight (kg) and distance (km).
    Rate: 0.5 per kg per km.
    Raises ValueError for invalid inputs.
    """
    if weight <= 0:
        raise ValueError(f"Weight must be positive, got {weight}")
    if distance < 0:
        raise ValueError(f"Distance cannot be negative, got {distance}")
    rate = 0.5
    return weight * distance * rate


def apply_discount(price: float, discount_pct: float) -> float:
    """
    Apply a discount percentage to a price.
    discount_pct must be between 0 and 100.
    """
    if not (0 <= discount_pct <= 100):
        raise ValueError(f"Discount must be 0-100, got {discount_pct}")
    return price - (price * discount_pct / 100)


def final_price(weight: float, distance: float, discount: float) -> float:
    """Calculate final shipping price after discount :) """
    shipping = calculate_shipping(weight, distance)
    return apply_discount(shipping, discount)
