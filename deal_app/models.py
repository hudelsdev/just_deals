from django.db import models
from django.contrib.auth.models import User
from datetime import time
from django.core.exceptions import ValidationError
from accounts_app.models import*


def validate_time_format(value):
  try:
    # Assuming your time fields are TimeFields
    time.fromisoformat(value)  # Attempt conversion (ISO format)
  except ValueError:
    raise ValidationError('Invalid time format. Use HH:MM format.')

# Create your models here.

class RegisterDealer(models.Model):
    drop_merchant_type =(
      ("hotel", "Hotel"),
      ("restuarent", "Restuarent"),
      ("spa", "Spa"),
      ("saloon", "Saloon")


    )

    user = models.OneToOneField(Dealer,on_delete=models.CASCADE,null=True)
    merchant_name = models.CharField(max_length=255)
    merchant_type=models.CharField(choices=drop_merchant_type, null=True,max_length=30)
    merchant_address=models.CharField(null=True,max_length=30)
    city=models.CharField(null=True,max_length=40)
    phone=models.IntegerField(null=True)


class Outlet(models.Model):
  user = models.OneToOneField(Dealer, on_delete=models.CASCADE, null=True, unique=True)  # Ensure only one outlet per dealer
  item_name = models.CharField(max_length=255, null=True,blank=True)
  description = models.TextField(null=True, blank=True)
  start_time = models.TimeField() 
  end_time = models.TimeField()  # Add validator
  item_img = models.ImageField(upload_to='images/', blank=True)  # Assuming image storage
  item_price = models.IntegerField(null=True, blank=True, default=0)  # Provide default value
  about = models.TextField(null=True, blank=True, default='')  # Provide default value
  

##model for outlet details

# class OutletFields(models.Model):
#   outlet = models.OneToOneField(Outlet, on_delete=models.CASCADE,null=True, related_name='fields')
#   item_price = models.IntegerField(null=True, blank=True, default=0)  # Provide default value
#   about = models.TextField(null=True, blank=True, default='')  # Provide default value
#   item_img = models.ImageField(upload_to='images/', blank=True)