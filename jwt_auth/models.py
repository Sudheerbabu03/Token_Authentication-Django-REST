from django.db import models


class Employee(models.Model):
    name=models.CharField(max_length=100)
    role=models.CharField(max_length=20)
    email=models.EmailField(max_length=100)
    mobile_no=models.CharField(max_length=20)
    salary=models.FloatField()
    location=models.CharField(max_length=100)




    
        
    
        
    

# Create your models here.
