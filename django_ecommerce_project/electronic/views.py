from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Wishlist, CartItem ,Order , OrderItem
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .sqs_utils import send_message_to_sqs
from electronic.models import Wishlist
from electronic.models import Cart
from django.contrib import messages
from library.cart_utils import calculate_total_price
from library.product_utils import format_product_name, validate_product_price
import sys
from .dynamodb_models import DynamoOrder  
import os
from django.contrib import messages
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'library'))
from .cloudwatch_utils import log_wishlist_addition
from .utils import send_cart_notification
from .forms import CheckoutForm
from .forms import OrderForm
from .sqs_utils import send_message_to_sqs


def home(request):
    products = Product.objects.all()
    return render(request, 'electronic/home.html', {'products': products})

def admin_login(request):
    return redirect('/admin/login/')  

def product_list(request):
    products = Product.objects.all()  # Retrieve all products from the database
    return render(request, 'electronic/productlist.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            quantity = int(request.POST.get('quantity', 1))  # Get the quantity from the form
            cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
            if created:
                cart_item.quantity = quantity
            else:
                cart_item.quantity += quantity  # If product already in the cart, increase the quantity
            cart_item.save()
            return redirect('cart')  # Redirect to the cart after adding the product

    return render(request, 'electronic/product_detail.html', {'product': product})

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose a different one.")
            return redirect('signup')  # Redirect to the sign-up page

        # Create the new user if the username is unique
        user = User.objects.create_user(username=username, password=password)
        messages.success(request, "Account created successfully! Please log in.")
        return redirect('login')
    return render(request, 'electronic/signup.html')
def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'electronic/login.html', {'error': 'Invalid credentials'})
    return render(request, 'electronic/login.html')

@login_required
def add_to_cart(request, product_id):
    # Get the product from the database
    product = get_object_or_404(Product, id=product_id)
    
    # Create or get the user's cart
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    # Check if the product is already in the cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not created:
        # If the product is already in the cart, increase the quantity
        cart_item.quantity += 1
        cart_item.save()
    else:
        # If it's a new product, set the quantity
        cart_item.quantity = 1
        cart_item.save()

    # Send SNS notification when product is added to the cart
    send_cart_notification(request.user.email, product.name)
    
    # Redirect to the cart page
    return redirect('cart')


@login_required
def add_to_wishlist(request, product_id):
    # Retrieve the product based on the ID
    product = get_object_or_404(Product, id=product_id)
    
    # Add the product to the user's wishlist
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.products.add(product)
    
    # Log the addition of this product to CloudWatch as a metric
    log_wishlist_addition(product.name)  # Send custom metric to CloudWatch

    return redirect('wishlist')  # Redirect to the wishlist page

def wishlist(request):
    # Get the wishlist for the current user
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    
    # Fetch all the products in the wishlist
    wishlist_items = wishlist.products.all()
    
    # Render the wishlist template with the items
    return render(request, 'electronic/wishlist.html', {'wishlist_items': wishlist_items})

def add_to_wishlist(request, product_id):
    # Get the product to add to wishlist
    product = get_object_or_404(Product, id=product_id)
    
    # Get the user's wishlist (create if it doesn't exist)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    
    log_wishlist_addition(product.name) 
    
    # If the product is already in the wishlist, notify the user
    if product in wishlist.products.all():
        messages.info(request, f"{product.name} is already in your wishlist.")
    else:
        wishlist.products.add(product)  # Add product to wishlist
        messages.success(request, f"Added {product.name} to your wishlist.")
    
    return redirect('wishlist')  # Redirect to the wishlist page

def cart(request):
    cart_items = CartItem.objects.filter(cart__user=request.user)

    # Calculate total price using the custom library function
    total_price = calculate_total_price(cart_items)

    return render(request, 'electronic/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })
@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.products.remove(product) 
    return redirect('wishlist')

@login_required
def remove_from_cart(request, item_id):
    # Get the cart item by its ID
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)

    # Delete the cart item
    cart_item.delete()

    # Redirect back to the cart
    return redirect('cart')
    
@login_required
def checkout(request):
    # Get all cart items for the logged-in user
    cart_items = CartItem.objects.filter(cart__user=request.user)

    if not cart_items:
        messages.error(request, "Your cart is empty. Add items to the cart before proceeding.")
        return redirect('cart')

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Create the order without saving it yet
            order = form.save(commit=False)
            order.user = request.user  # Associate the order with the logged-in user
            order.status = 'Delivered'  # Set default status (can be changed later)
            order.save()

            # Create OrderItem objects for each CartItem
            for cart_item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    price=cart_item.product.price
                )

            # Clear the cart after placing the order
            cart_items.delete()

            messages.success(request, 'Your order has been placed successfully!')
            return redirect('order_confirmation', order_id=order.id)
    else:
        form = CheckoutForm()

    return render(request, 'electronic/checkout.html', {'form': form})
@login_required
def orders(request):
    # Get all orders placed by the logged-in user
    orders = Order.objects.filter(user=request.user).order_by('-order_date')

    # Add the total price for each order
    for order in orders:
        order.total_price = sum(item.price * item.quantity for item in order.order_items.all())

    return render(request, 'electronic/orders.html', {'orders': orders})
    
@login_required
def order_confirmation(request, order_id):
    # Try to fetch the order from DynamoDB using product_id (order_id in this case)
    try:
        dynamo_order = DynamoOrder(product_id=order_id)  # Use order_id as the product_id
        order_data = dynamo_order.get_order()  # Fetch order data from DynamoDB
    except Exception as e:
        order_data = None
        print(f"Error fetching order from DynamoDB: {e}")

    if order_data is None:
        # If order is not found in DynamoDB, fallback to fetching from the relational database
        order = get_object_or_404(Order, id=order_id, user=request.user)
        order_items = OrderItem.objects.filter(order=order)
        total_price = sum(item.quantity * item.price for item in order_items)

        # Render order confirmation page with order details from the relational database
        return render(request, 'electronic/order_confirmation.html', {
            'order': order,
            'order_items': order_items,
            'total_price': total_price,
        })
    else:
        # If the order is found in DynamoDB, use the data from DynamoDB
        total_price = order_data.get('total_price', 0)  # Fallback to 0 if total_price is missing
        order_items = []  # You can adjust this part to match how you want to show order items from DynamoDB

        # Render order confirmation page with order data from DynamoDB
        return render(request, 'electronic/order_confirmation.html', {
            'order': order_data,  # Order details from DynamoDB
            'order_items': order_items,
            'total_price': total_price,
        })
@login_required
def place_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            # Save the order to the relational database (SQLite/MySQL/PostgreSQL)
            order = form.save(commit=False)
            order.user = request.user
            order.save()  # Save the order in the Django database

            # Now save the same order to DynamoDB using DynamoOrder
            dynamo_order = DynamoOrder(
                product_id=str(order.id),  # Use the order ID as the product_id (Partition key)
                user=str(order.user.id),    # Store the user ID as a string
                total_price=str(order.total_price),  # Convert total_price to string
                order_date=str(order.order_date)  # Convert order_date to string (ISO format)
            )
            # Save the order to DynamoDB
            dynamo_order.save()

            # Send order details to SQS
            order_message = f"Order ID: {order.id}, User: {order.user.username}, Total Price: €{order.total_price}"
            send_message_to_sqs(order_message)  # Send to SQS

            return redirect('order_confirmation', order_id=order.id)

    else:
        form = OrderForm()

    return render(request, 'place_order.html', {'form': form})