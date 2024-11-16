from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Product, Wishlist, CartItem, Order, OrderItem


admin.site.register(Product)
admin.site.register(Wishlist)
admin.site.register(CartItem)
admin.site.register(OrderItem)
admin.site.register(Order)



class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'image')
    list_editable = ('price', 'quantity')
    search_fields = ('name',)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0  # This will prevent extra empty fields
# OrderAdmin class to customize the admin interface for Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order_date', 'status', 'total_price')
    inlines = [OrderItemInline]  # Displays order items inline with the order

    def total_price(self, obj):
        # This function calculates the total price of the order by summing the prices of the items in the order
        return sum(item.price * item.quantity for item in obj.order_items.all())
    total_price.short_description = 'Total Price'
















