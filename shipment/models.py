import uuid
from django.conf import settings
from django.db import models
from accounts.models import CustomerUser, User, DriverUser

# Create your models here.

class Ship(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    assigned_driver = models.ForeignKey(DriverUser, on_delete=models.CASCADE, null=True, blank=True)
    of_type = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    package_type = models.CharField(max_length=100)
    start = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    delivery_date = models.CharField(max_length=100)
    payment_type = models.CharField(max_length=100)
    tracking_number = models.UUIDField(default=uuid.uuid4, editable=False)



class TrackingModel(models.Model):
    assigned_driver = models.ForeignKey(DriverUser, on_delete=models.CASCADE, null=True, blank=True) 
    tracking_number = models.UUIDField()
    driver_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)



