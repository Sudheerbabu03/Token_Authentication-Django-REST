from django.db import models
from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):
    emp_id=models.CharField(max_length=50,primary_key=True)
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    role=models.CharField(max_length=20)
    email=models.EmailField(max_length=100)
    mobile_no=models.CharField(max_length=20)
    salary=models.FloatField()
    location=models.CharField(max_length=100)
    USERNAME_FIELD="emp_id"
    EMAIL_FIELD="email"
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='employee_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='employee_permissions',
        blank=True
    )
    




    
        
    
        
    

# Create your models here.
