def calculate_shipping(weight, distance):
    if weight <= 0:
        raise ValueError("Weight must be positive")
    if distance < 0:
        raise ValueError("Distance cannot be negative")
    rate = 0.5
    return weight * distance * rate


def apply_discount(price, discount_pct):
    if discount_pct < 0 or discount_pct > 100:
        raise ValueError("Discount must be 0-100 !!!!")
    return price - (price * discount_pct / 100)


def express_shipping(weight, distance):
    """Express shipping costs twice the standard rate."""
    return calculate_shipping(weight, distance) * 2


def final_price(weight, distance, discount):
    shipping = calculate_shipping(weight, distance)
    return apply_discount(shipping, discount)
