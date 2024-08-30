from django.shortcuts import render
from django.contrib import messages
from .models import Vendor
import uuid

def vendor_register(request):
    if request.method == 'POST':
        # Extract form data from POST request
        vendor_name = request.POST.get('fname')
        vendor_type = request.POST.get('vendor_type')
        point_of_contact = request.POST.get('point_of_contact')
        phone = request.POST.get('phone')
        terms = request.POST.get('terms')
        uname = request.POST.get('uname')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        
        # Extract new form fields
        account_holder_name = request.POST.get('account_holder_name')
        bank_name = request.POST.get('bank_name')
        branch = request.POST.get('branch')
        account_number = request.POST.get('account_number')
        ifsc_code = request.POST.get('ifsc_code')
        commission_percentage = request.POST.get('commission_percentage')
        
        # Handle file upload
        image = request.FILES.get('image')

        # Validate that passwords match
        if password != cpassword:
            messages.error(request, "Passwords do not match.")
            return render(request, 'vendor_register.html', {
                'temp_unique_id': uuid.uuid4().hex[:8].upper(),
                'choices': Vendor.VENDOR_TYPE_CHOICES
            })

        # Validate commission percentage
        try:
            # Check if commission_percentage is not None or empty
            if commission_percentage:
                commission_percentage = float(commission_percentage)
                if commission_percentage < 0 or commission_percentage > 100:
                    raise ValueError("Commission percentage must be between 0 and 100.")
            else:
                commission_percentage = 0.00  # Set a default value or handle as needed
        except ValueError as e:
            messages.error(request, str(e))
            return render(request, 'vendor_register.html', {
                'temp_unique_id': uuid.uuid4().hex[:8].upper(),
                'choices': Vendor.VENDOR_TYPE_CHOICES
            })

        # Check if the username already exists
        if Vendor.objects.filter(uname=uname).exists():
            messages.error(request, "Username already exists. Please choose a different username.")
            return render(request, 'vendor_register.html', {
                'temp_unique_id': uuid.uuid4().hex[:8].upper(),
                'choices': Vendor.VENDOR_TYPE_CHOICES
            })

        # Create a new vendor instance
        vendor = Vendor(
            fname=vendor_name,
            vendor_type=vendor_type,
            point_of_contact=point_of_contact,
            phone=phone,
            terms=terms,
            image=image,
            uname=uname,
            password=password,  # Note: Consider using Django's built-in User model for authentication
            cpassword=cpassword,  # This should be used only for validation; consider not storing it.
            account_holder_name=account_holder_name,
            bank_name=bank_name,
            branch=branch,
            account_number=account_number,
            ifsc_code=ifsc_code,
            commission_percentage=commission_percentage
        )

        # Save the vendor to the database
        vendor.save()

        # Capture the unique ID
        unique_id = vendor.pk  # Assuming `pk` is the unique identifier for the Vendor instance

        # Pass the unique ID to the success page
        messages.success(request, f"Vendor registered successfully. Your unique ID is {unique_id}.")
        return render(request, 'index.html', {'unique_id': unique_id})

    else:
        # Generate a temporary unique ID for the registration form
        temp_unique_id = uuid.uuid4().hex[:8].upper()

    # Render the form page with the temporary unique ID and vendor type choices
    return render(request, 'vendor_register.html', {
        'temp_unique_id': temp_unique_id,
        'choices': Vendor.VENDOR_TYPE_CHOICES
    })
