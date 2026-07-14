from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CompanyForm
from .models import Company


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