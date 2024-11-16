# shop/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    try:
        return value * arg
    except (TypeError, ValueError):
        return 0

# Custom filter to sum the values of a list
@register.filter
def sum_items(value):
    return sum(value)
    
