from django.shortcuts import render, redirect, get_object_or_404
from decimal import Decimal
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from companies.models import Company
from .forms import BuySharesForm, SellSharesForm
from .models import Portfolio
from transactions.models import Transaction

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

            Transaction.objects.create(
                user=request.user,
                company=company,
                transaction_type=Transaction.BUY,
                quantity=quantity,
                price=buy_price,
            )
                
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

@login_required
def portfolio_list(request):

    portfolios = Portfolio.objects.filter(
        user=request.user
    ).select_related("company")

    return render(
        request,
        "portfolio/portfolio_list.html",
        {
            "portfolios": portfolios,
        },
    )

@login_required
def sell_shares(request, portfolio_id):

    portfolio = get_object_or_404(
        Portfolio,
        id=portfolio_id,
        user=request.user,
    )

    if request.method == "POST":

        form = SellSharesForm(request.POST)

        if form.is_valid():

            quantity = form.cleaned_data["quantity"]

            if quantity > portfolio.quantity:

                messages.error(
                    request,
                    "You don't have enough shares to sell."
                )

            elif quantity == portfolio.quantity:
                Transaction.objects.create(
                    user=request.user,
                    company=portfolio.company,
                    transaction_type=Transaction.SELL,
                    quantity=quantity,
                    price=portfolio.company.current_price,
                )

                portfolio.delete()

                messages.success(
                    request,
                    "All shares sold successfully."
                )

                return redirect("portfolio:portfolio_list")

            else:

                portfolio.quantity -= quantity

                portfolio.save()
                Transaction.objects.create(
                    user=request.user,
                    company=portfolio.company,
                    transaction_type=Transaction.SELL,
                    quantity=quantity,
                    price=portfolio.company.current_price,
                )

                messages.success(
                    request,
                    "Shares sold successfully."
                )

                return redirect("portfolio:portfolio_list")

    else:

        form = SellSharesForm()

    return render(
        request,
        "portfolio/sell_shares.html",
        {
            "form": form,
            "portfolio": portfolio,
        },
    )
