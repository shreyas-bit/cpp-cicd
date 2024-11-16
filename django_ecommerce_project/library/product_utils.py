# library/product_utils.py

def format_product_name(name):
    return name.capitalize()  # Example function

def validate_product_price(price):
    if price < 0:
        raise ValueError("Price cannot be negative.")
    return price  # Example function
