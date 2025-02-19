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





