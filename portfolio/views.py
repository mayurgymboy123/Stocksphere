from django.shortcuts import render, redirect, get_object_or_404
from decimal import Decimal
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from companies.models import Company
from .forms import BuySharesForm
from .models import Portfolio

@login_required
def buy_shares(request, company_id):
    company = get_object_or_404(
            Company,
            id=company_id
        )
    if request.method == "POST":
        form = BuySharesForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data["quantity"]
            buy_price = form.cleaned_data["buy_price"]
            portfolio, created = Portfolio.objects.get_or_create(
                user=request.user,
                company=company,
                defaults={
                    "quantity": quantity,
                    "average_buy_price": buy_price,
                },
            )
            if not created:
                total_cost = (portfolio.quantity * portfolio.average_buy_price) + (quantity * buy_price)
                total_quantity = (portfolio.quantity + quantity)
                portfolio.average_buy_price = (total_cost/total_quantity)
                portfolio.quantity = total_quantity
                portfolio.save()
                
            messages.success(
                request,
                "Shares Purchased Successfully."
            )

            return redirect("companies:company_list")
        
    else:
        form = BuySharesForm()

    return render(
        request,
        "portfolio/buy_shares.html",
        {
            "form": form,
            "company": company,
        },
    )
