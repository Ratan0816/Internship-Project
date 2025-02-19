from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)  
    
    def __str__(self):
        return self.name


class Role(models.Model):
    r_name=models.CharField(max_length=100)  
    r_description=models.CharField(max_length=200)  
    r_created_at=models.DateTimeField(auto_now_add=True)  
    r_updated_at=models.DateTimeField(auto_now=True) 
    r_status=models.BooleanField(default=True)  
    
    def __str__(self):
        return self.r_name


class Employee(User):
    employee_id = models.AutoField(primary_key=True)
    f_name = models.CharField(max_length=100)
    username=models.CharField(max_length=100, unique=True)
    password=models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    mobile = models.CharField(max_length=100)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, blank=True)
    role = models.ForeignKey('Role', on_delete=models.SET_NULL, null=True, blank=True)
    reporting_manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    date_of_joining = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.f_name} {self.l_name}"



