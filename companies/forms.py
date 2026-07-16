from django import forms
from .models import Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            "name",
            "symbol",
            "logo",
            "current_price",
            "exchange",
            "sector",
            "industry",
            "currency",
            "country",
        ]
        
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Company Name"
            }),
            "symbol": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Stock Symbol"
            }),
            "logo": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "current_price": forms.NumberInput(attrs={
                "class": "form-control",
                "step": "0.01"
            }),
            "exchange": forms.Select(attrs={
                "class": "form-select"
            }),
            "sector": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Sector"
            }),
            "industry": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Industry"
            }),
            "currency": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "country": forms.TextInput(attrs={
                "class": "form-control"
            }),
        }