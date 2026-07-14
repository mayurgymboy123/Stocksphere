from django.urls import path
from . import views
app_name = "companies"
urlpatterns = [
    path("",views.company_list,name="company_list"),
    path("create/",views.create_company,name="create_company"),
    path("<int:company_id>/edit/",views.edit_company,name="edit_company")
]