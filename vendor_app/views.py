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
        
        # Handle file upload
        image = request.FILES.get('image')

        # Validate that passwords match
        if password != cpassword:
            messages.error(request, "Passwords do not match.")
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
            password=password,
            cpassword=cpassword,  # Note: This should be used only for validation; consider not storing it.
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
