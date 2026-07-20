from django.urls import path
from . import views
app_name = "companies"
urlpatterns = [
    path("",views.company_list,name="company_list"),
    path("create/",views.create_company,name="create_company"),
    path("<int:company_id>/edit/",views.edit_company,name="edit_company"),
    path("search/", views.search_companies, name="search_companies"),
    path("<int:pk>/", views.company_detail, name="company_detail"),
    path("import/<str:symbol>/", views.import_company, name="import_company"),
]