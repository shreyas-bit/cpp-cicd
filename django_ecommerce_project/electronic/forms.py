# forms.py
from django import forms
from .models import Order

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'phone_number', 'address', 'email']  # Fields to be filled by the user

    def save(self, commit=True):
        # Custom save logic, if necessary
        order = super().save(commit=False)  # Create Order object without saving yet
        if commit:
            order.save()  # Save the order to the database
        return order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'phone_number', 'address', 'email']  # Add the fields you need