from django.urls import path
from .views import DepartmentCreate,DepartmentUpdate,DepartmentDelete,DepartmentList

urlpatterns = [
    path('create/',DepartmentCreate.as_view(),name='create_department' ),
    path('list/',DepartmentList.as_view(),name='list_department' ),
    path('update/<int:pk>/',DepartmentUpdate.as_view(),name='update_department' ),
    path('delete/<int:pk>/',DepartmentDelete.as_view(),name='delete_department' ),
]
