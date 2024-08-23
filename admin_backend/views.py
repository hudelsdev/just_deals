from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from deal_app.models import*
from django.shortcuts import render, get_object_or_404
from admin_backend.decorators import super_login_required



# Create your views here.

def super_admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Login Success")
            return redirect('admin_index')
        else:
            messages.error(request, "Invalid username or password")
    
    
    if request.user.is_authenticated:
        return redirect('admin_index')

    return render(request, 'super_admin_login.html')



def super_admin_logout(request):
    logout(request)
    messages.success(request, "Logout successful")
    return redirect('super_admin_login') 

# @super_login_required
def dealer_vouchers(request):
    # Get the dealer associated with the logged-in user
    try:
        dealer = Dealers.objects.get(user=request.user)
    except Dealers.DoesNotExist:
        # Handle the case where no dealer is associated with the user
        return render(request, 'outlet_list.html', {'message': 'No dealer profile found for the logged-in user.'})
    
    # Retrieve all vouchers associated with this dealer
    items = Voucher.objects.filter(dealer=dealer)

    return render(request, 'outlet_list.html', {'items': items})



def voucher_items_edit(request, pk):
    # Get the voucher associated with the given primary key
    voucher = get_object_or_404(Voucher, pk=pk)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'save':
            # Process save
            name = request.POST.get('voucher_name')
            description = request.POST.get('voucher_description')
            price = request.POST.get('voucher_price')
            about = request.POST.get('voucher_about')

            # Update fields
            voucher.voucher_name = name
            voucher.voucher_description = description
            voucher.voucher_price = price
            voucher.voucher_about = about

            # Uncomment if you use image upload
            # image = request.FILES.get('image')
            # if image:
            #     voucher.item_img = image

            voucher.save()
            return redirect('dealer_vouchers')
        elif action == 'cancel':
            # Redirect without saving
            return redirect('dealer_vouchers')

    return render(request, 'voucher_edit.html', {'edit_items': voucher})


def voucher_items_delete(request, pk):
    # Get the voucher associated with the given primary key
    voucher = get_object_or_404(Voucher, pk=pk)

    if request.method == 'POST':
        voucher.delete()
        return redirect('dealer_vouchers')
    else:
        # Typically, a GET request to this endpoint should be handled differently,
        # but in this case, we just redirect to the dealer_vouchers without deleting anything.
        return redirect('dealer_vouchers')