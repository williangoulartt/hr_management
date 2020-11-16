from django.urls import path
from .views import (
    EmployeeCreate,
    EmployeesList,
    EmployeeDelete,
    EmployeeUpdate,
)

urlpatterns = [
    path('create/',EmployeeCreate.as_view(),name='create_employee'),
    path('list/',EmployeesList.as_view(),name='list_employees'),
    path('delete/<int:pk>/',EmployeeDelete.as_view(),name='delete_employee'),
    path('update/<int:pk>/',EmployeeUpdate.as_view(),name='update_employee'),
]
