from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .services import DashboardService


@login_required
def dashboard(request):
    context = {
        "holdings": DashboardService.get_holdings(request.user)
    }
    return render(
        request,
        "dashboard/dashboard.html",
        context,
    )