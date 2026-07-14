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
            "description",
            "is_active",
        ]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter company name",
                }
            ),
            "symbol": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter stock symbol",
                }
            ),
            "current_price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter current price",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Enter company description",
                }
            ),
            "logo": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }