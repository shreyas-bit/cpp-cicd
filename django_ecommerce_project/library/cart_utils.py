# library/cart_utils.py

# library/cart_utils.py

def calculate_total_price(cart_items):
    """
    This function calculates the total price for a list of cart items.
    """
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return total_price


def get_cart_item_count(cart_items):
    """Return the total number of items in the cart."""
    return sum(item.quantity for item in cart_items)
