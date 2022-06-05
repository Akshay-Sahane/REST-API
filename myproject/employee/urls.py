from django.urls import path
from .views import *

urlpatterns = [
    path('emp/',EmpList.as_view()), #url to only show emp data
    path('empadd/',EmpCreate.as_view()), #url to add new employee.
    path('emp/<int:pk>/',EmpRetrieveUpdateDestroy.as_view()), #path to retrieve,update or delete employee with specified pk.
]