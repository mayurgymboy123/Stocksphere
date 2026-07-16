from django import template

register = template.Library()


@register.filter
def indian_currency(value):

    if value is None:
        return "₹0"

    value = float(value)

    if value >= 10000000:
        return f"₹{value / 10000000:.2f} Cr"

    elif value >= 100000:
        return f"₹{value / 100000:.2f} Lakh"

    else:
        return f"₹{value:,.2f}"