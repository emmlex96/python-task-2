# PSEUDOCODE:
# Define function apply_discount(item_name, original_price, promo_code)
#   If promo_code is "SAVE10" → discount = 10% of original_price
#   If promo_code is "HALFOFF" → discount = 50% of original_price
#   Otherwise → no discount
#   Return original_price - discount

def apply_discount(item_name, original_price, promo_code=""):
    if original_price < 0:
        raise ValueError("Price cannot be negative")

    if promo_code == "SAVE10":
        discount = original_price * 0.10
    elif promo_code == "HALFOFF":
        discount = original_price * 0.50
    else:
        discount = 0

    return round(original_price - discount, 2)
