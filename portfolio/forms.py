from django import forms

class BuySharesForm(forms.Form):

    quantity = forms.IntegerField(
        min_value=1
    )

    buy_price = forms.DecimalField(
        max_digits=10,
        decimal_places=2
    )
class SellSharesForm(forms.Form):

    quantity = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter quantity to sell",
            }
        )
    )