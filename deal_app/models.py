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
    raise ValidationError('Invalid time for mat. Use HH:MM format.')

# Create your models here.

class Dealers(models.Model):
    drop_merchant_type =(
      ("hotel", "Hotel"),
      ("restuarent", "Restuarent"),
      ("spa", "Spa"),
      ("saloon", "Saloon")


    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, unique=True)
    merchant_name = models.CharField(max_length=255)
    business_owner_name = models.CharField(max_length=255, default='')
    merchant_type = models.CharField(choices=drop_merchant_type, max_length=30, null=True)
    merchant_address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=40, null=True)
    phone = models.BigIntegerField(null=True)
    contact_person = models.IntegerField(null=True,blank=True)

    outlet_name = models.CharField(max_length=255, null=True, blank=True)
    outlet_description = models.TextField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    outlet_img = models.ImageField(upload_to='images/', blank=True)
   


class Voucher(models.Model):
    dealer = models.ForeignKey(Dealers, on_delete=models.CASCADE, null=True, blank=True)
    voucher_name =models.CharField(max_length=255, blank=True, null=True)  # Optional, allows empty strings and NULLs
    voucher_price = models.IntegerField(default=0)  # Default value of 0, no need for null=True
    voucher_about = models.TextField(blank=True, default='')  # Default value of an empty string
    voucher_description = models.TextField(blank=True, default='')  
    button_link = models.URLField(blank=True, null=True)  # Add this line for button link
    voucher_date = models.DateField(null=True, blank=True)

class VoucherCoupon(models.Model):
    coupon_name = models.CharField(max_length=255, null=True, default='')
    coupon_description = models.TextField(blank=True, null=True, default='')
    coupon_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    coupon_button_link = models.URLField(max_length=200, blank=True, null=True)
