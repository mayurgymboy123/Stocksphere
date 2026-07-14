from django import forms

class BuySharesForm(forms.Form):

    quantity = forms.IntegerField(
        min_value=1
    )

    buy_price = forms.DecimalField(
        max_digits=10,
        decimal_places=2
    )