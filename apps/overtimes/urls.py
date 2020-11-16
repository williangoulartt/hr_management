from django.urls import path
from .views import (
    OverTimeCreate,
    OverTimeList,
    OverTimeEdit,
    OverTimeDelete,
)

urlpatterns = [
    path('new/',OverTimeCreate.as_view(),name='create_overtime' ),
    path('list/',OverTimeList.as_view(),name='list_overtime' ),
    path('edit/<int:pk>',OverTimeEdit.as_view(),name='edit_overtime' ),
    path('delete/<int:pk>',OverTimeDelete.as_view(),name='delete_overtime' ),
]
