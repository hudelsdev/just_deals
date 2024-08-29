from django.db import models

class Vendor(models.Model):
    VENDOR_TYPE_CHOICES = [
        ('individual', 'Individual'),
        ('company', 'Company'),
        # Add more vendor types as needed
    ]
    
    # Vendor name
    fname = models.CharField(max_length=255)

    # Vendor type
    vendor_type = models.CharField(max_length=50, choices=VENDOR_TYPE_CHOICES)

    # Point of contact
    point_of_contact = models.CharField(max_length=255)

    # Phone
    phone = models.CharField(max_length=15)

    # Vendor logo (image field)
    image = models.ImageField(upload_to='vendor_logos/', blank=True, null=True)

    # Terms and conditions
    terms = models.TextField()

    # Username
    uname = models.CharField(max_length=150, unique=True)

    # Password
    password = models.CharField(max_length=128)  # Consider using Django's built-in User model for authentication

    # Confirm password (not stored in the model, used for validation only)
    cpassword = models.CharField(max_length=128)

    def __str__(self):
        return self.fname
