from django.db import models

# Employee model/table
class Employee(models.Model):
    empid=models.AutoField(primary_key=True)
    empname=models.CharField(max_length=100)
    empage=models.IntegerField()