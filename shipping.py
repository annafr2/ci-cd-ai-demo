EXPRESS_MULTIPLIER = 2


def calculate_shipping(weight, distance):
    """Calculate shipping cost based on weight (kg) and distance (km)."""
    if weight <= 0:
        raise ValueError("Weight must be positive")
    if distance < 0:
        raise ValueError("Distance cannot be negative")
    rate = 0.5
    return weight * distance * rate


def express_shipping(weight, distance):
    """Calculate express shipping cost (double the standard rate)."""
    return calculate_shipping(weight, distance) * EXPRESS_MULTIPLIER


def apply_discount(price, discount_pct):
    """Apply a percentage discount (0–100) to a price."""
    if discount_pct < 0 or discount_pct > 100:
        raise ValueError("Discount must be 0-100..")
    return price - (price * discount_pct / 100)


def final_price(weight, distance, discount, express=False):
    """Return the final shipping price after applying a discount.
    
    If express=True, apply express (x2) rate before discount.
    """
    if express:
        shipping = express_shipping(weight, distance)
    else:
        shipping = calculate_shipping(weight, distance)
    return apply_discount(shipping, discount)

