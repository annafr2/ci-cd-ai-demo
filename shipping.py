# ⚠️  DEMO VERSION — intentionally missing input validation
# For the "break the pipeline" demo:
#   1. Copy the contents of THIS file into shipping.py
#   2. git add . && git commit -m "oops" && git push  → watch pipeline go RED ❌
#   3. Then paste back the original shipping.py contents  → pipeline goes GREEN ✅

def calculate_shipping(weight, distance):
    rate = 0.5
    return weight * distance * rate   # BUG: no validation for negative/zero inputs


def apply_discount(price, discount_pct):
    return price - (price * discount_pct / 100)  # BUG: no bounds check on discount


def final_price(weight, distance, discount):
    shipping = calculate_shipping(weight, distance)
    return apply_discount(shipping, discount)
