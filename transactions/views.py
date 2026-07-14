from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Transaction


@login_required
def transaction_list(request):

    transactions = (
        Transaction.objects
        .filter(user=request.user)
        .select_related("company")
    )

    return render(
        request,
        "transactions/transaction_list.html",
        {
            "transactions": transactions,
        },
    )