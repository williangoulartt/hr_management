from django.urls import path
from .views import CompanyCreate,CompanyEdit


urlpatterns = [
    path('new',CompanyCreate.as_view(),name='create_company' ),
    path('edit/<int:pk>/',CompanyEdit.as_view(),name='edit_company' ),
]
