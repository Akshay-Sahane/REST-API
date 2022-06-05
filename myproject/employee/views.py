from apis.serializers import EmployeeSerializer
from .models import Employee
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from apis.customauth import CustomAuth,CustomAuthForOnlyView

# through admin panel superuser can add groups to user for specific permissions

# to display all employee data.
class EmpList(ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated,CustomAuthForOnlyView]

# to create/add new employee.
class EmpCreate(CreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated,CustomAuth]

# to retrieve or update or delete a single employee object.
class EmpRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated,CustomAuth]