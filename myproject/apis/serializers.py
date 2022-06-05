from dataclasses import field
from statistics import mode
from rest_framework import serializers
from employee.models import Employee

# this serializer is used to convert queryset of emp-data to python data type. 
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=['empid','empname','empage']