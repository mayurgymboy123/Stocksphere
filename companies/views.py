from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CompanyForm
from .models import Company
from django.http import JsonResponse
from companies.services.stock_service import StockService
from companies.services.company_import_service import CompanyImportService
from companies.services.yahoo_service import YahooFinanceService


# Create your views here.
@login_required
def create_company(request):
    if request.method == "POST":
        form = CompanyForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Company created successfully.")
            return redirect("companies:company_list")
    else:
        form = CompanyForm()
    return render(request, "companies/create_company.html", {"form": form})

@login_required
def company_list(request):
    companies = Company.objects.all()

    return render(
        request,
        "companies/company_list.html",
        {
            "companies":companies
        }
    )

@login_required
def edit_company(request, company_id):

    company = get_object_or_404(
        Company,
        id=company_id
    )

    if request.method == "POST":

        form = CompanyForm(
            request.POST,
            request.FILES,
            instance=company
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Company updated successfully."
            )

            return redirect("companies:company_list")

    else:

        form = CompanyForm(
            instance=company
        )

    return render(
        request,
        "companies/edit_company.html",
        {
            "form": form,
            "company": company,
        }
    )

def search_companies(request):
    query = request.GET.get("q", "").strip()

    if not query:
        return JsonResponse({
            "success": False,
            "results": []
        })

    result = StockService.search_companies(query)

    return JsonResponse(result)

@login_required
def company_detail(request, pk):
    company = get_object_or_404(
        Company,
        pk=pk,
        is_active=True,
    )

    context = {
        "company": company,
    }

    return render(
        request,
        "companies/company_detail.html",
        context,
    )

@login_required
def import_company(request, symbol):
    company = CompanyImportService.import_company(symbol)

    if company:
        return redirect("companies:company_detail", pk=company.pk)

    return redirect("dashboard:dashboard")

def refresh_price(request, company_id):
    company = get_object_or_404(Company, id=company_id)

    if not company.yahoo_symbol:
        messages.error(request, "Yahoo symbol is not available for this company.")
        return redirect("companies:company_detail", company.id)

    result = YahooFinanceService.get_price(company.yahoo_symbol)

    if result["success"]:
        company.current_price = result["price"]
        company.save()
        messages.success(request, "Price updated successfully.")
    else:
        messages.error(request, result["error"])

    return redirect("companies:company_detail", company.id)