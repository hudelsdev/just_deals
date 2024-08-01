from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout


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