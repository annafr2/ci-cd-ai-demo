def calculate_shipping(weight, distance):
    """Calculate shipping cost based on weight (kg) and distance (km)."""
    if weight <= 0:
        raise ValueError("Weight must be positive")
    if distance < 0:
        raise ValueError("Distance cannot be negative")
    rate = 0.5
    return weight * distance * rate


def apply_discount(price, discount_pct):
    """Apply a percentage discount (0–100) to a price."""
    if discount_pct < 0 or discount_pct > 100:
        raise ValueError("Discount must be 0-100")
    return price - (price * discount_pct / 100)


def final_price(weight, distance, discount):
    """Return the final shipping price after applying a discount."""
    shipping = calculate_shipping(weight, distance)
    return apply_discount(shipping, discount)


def express_shipping(weight, distance):
    """Calculate express shipping cost — double the standard rate."""
    return calculate_shipping(weight, distance) * 2
