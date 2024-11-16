from django.contrib import admin
from django.contrib.auth import get_user_model 
from .models import Product, Wishlist, CartItem, Order, OrderItem


admin.site.register(Product)
admin.site.register(Wishlist)
admin.site.register(CartItem)





class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'image')
    list_editable = ('price', 'quantity')
    search_fields = ('name',)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0  # No extra empty rows by default

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order_date', 'status')  # Customize as needed
    inlines = [OrderItemInline]  # Shows order items in the order detail page
    
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)