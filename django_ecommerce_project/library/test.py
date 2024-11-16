# library/tests.py

from django.test import TestCase
from .cart_utils import calculate_total_price
from electronic.models import Product, CartItem, Cart
from django.contrib.auth.models import User

class CartUtilsTests(TestCase):
    def test_calculate_total_price(self):
        user = User.objects.create_user(username='testuser', password='password')
        product1 = Product.objects.create(name='Product 1', price=100)
        product2 = Product.objects.create(name='Product 2', price=150)

        cart = Cart.objects.create(user=user)
        CartItem.objects.create(cart=cart, product=product1, quantity=2)
        CartItem.objects.create(cart=cart, product=product2, quantity=1)

        cart_items = CartItem.objects.filter(cart=cart)
        total_price = calculate_total_price(cart_items)

        self.assertEqual(total_price, 350)  # (100 * 2) + (150 * 1) = 350
