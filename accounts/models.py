
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    username = models.CharField(max_length=100, unique=True) 
    phone = models.CharField(max_length=12, default="1233")
    license = models.CharField(max_length=100, null=True)
    vehicle_number = models.CharField(max_length=100, null=True)

# Create your models here.

class CustomerUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)  
    email = models.EmailField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    
class DriverUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)    
    email = models.EmailField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    license =models.CharField(max_length=100)
    vehicle_number = models.CharField(max_length=100, null=True)
    
