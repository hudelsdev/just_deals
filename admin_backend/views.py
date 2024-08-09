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

@super_login_required
def outlet_list(request):
    items = Outlet.objects.all()
    return render(request,'outlet_list.html',{'items':items} )


def outlet_items_edit(request, pk):
    outlet_items = get_object_or_404(Outlet, pk=pk)

    if request.method == 'POST':
        name = request.POST.get('item-name')
        description = request.POST.get('description')
        price = request.POST.get('item-price')
        time_from = request.POST.get('time-from')
        time_to = request.POST.get('time-to')
        about = request.POST.get('about')
        image = request.FILES.get('image')

        # Update fields
        outlet_items.item_name = name
        outlet_items.description = description
        outlet_items.item_price = price
        outlet_items.start_time = time_from
        outlet_items.end_time = time_to
        outlet_items.about = about
        
        if image:
            outlet_items.item_img = image
        
        outlet_items.save()
        return redirect('outlet_list')

    return render(request, 'outlet_items_edit.html', {'edit_items': outlet_items})


def outlet_items_delete(request, pk):
    outlet_item = get_object_or_404(Outlet, pk=pk)

    if request.method == 'POST':
        outlet_item.delete()
        return redirect('outlet_list')
    else:
        # Typically, a GET request to this endpoint should be handled differently,
        # but in this case, we just redirect to the outlet_list without deleting anything.
        return redirect('outlet_list')

