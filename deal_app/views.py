from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from deal_app.models import*
# from datetime import time
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from admin_backend.decorators import super_login_required
from django.shortcuts import render, redirect
from .models import Outlet
# from django.core.mail import send_mail
from django.contrib.auth import authenticate,login as auth_login,logout,login
# Create your views here.
@super_login_required
def dealer_index(request):
    dealerdatas = RegisterDealer.objects.all()
    return render(request, 'dealer_index.html', {'dealerdatas': dealerdatas})
    

def unauthorized(request):
    return render(request, 'unauthorized.html')

# views for registration /////////////
##############################here we need to cahange like jobportal company register#######
def deal_register(request):
    if request.method == 'POST':
        merchant_name = request.POST['merchant_name']
        merchant_type = request.POST['merchant_type']
        merchant_address = request.POST['merchant_address']
        city = request.POST['city']
        phone=request.POST['phone']
        user_name= request.POST['uname']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        # user=Dealer.objects.filter(username=user_name)
        if User.objects.filter(username=user_name):
            print('username is already exists') 

            return render(request,'deal_register.html')
        else:
            if (password != cpassword):
                print('password is not match')
                return render(request,'deal_register.html')
            else:
                 #create a new user
                user=User.objects.create_user(
                                          email=email,
                                          password=password,
                                          username=user_name
                                          )

                user.save()

                newdealer=RegisterDealer(user=user,phone=phone,merchant_type=merchant_type,city=city,merchant_name=merchant_name,merchant_address=merchant_address)
                newdealer.save()
                print("success")

                auth_login(request, user)
                return redirect('dealer_login')
           

    else:
        print('not registered')
        choices=RegisterDealer.drop_merchant_type
        return render(request,'deal_register.html' ,{'choices':choices})                       
    #     if not user:
    #         if password==cpassword:
    #             deal_user=Dealer.objects.create_user(username=user_name, password=cpassword, email=email,
    #                                         )
    #             deal_user.save()
    #             new_deal_user=RegisterDealer(merchant_type=merchant_type,merchant_name=merchant_name,merchant_address=merchant_address,city=city,phone=phone)
    #             new_deal_user.save()
                
    #             messages.success(request, "Account created successfully")
    #             return redirect('dealer_login')
    #         else:
    #             messages.success(request, "Password is incorrect")
    # choices=RegisterDealer.drop_merchant_type
    # return render(request,'deal_register.html' ,{'choices':choices})                       
            
# views for login page///////

def dealer_login(request):
    if request.method == 'POST':
        username=request.POST['uname']
        password=request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('add_fields')
        else:
            return render(request,'dealer_login.html')
    else:
        
        return render(request,"dealer_login.html")


#forgot password///////

def forgot_password(request):

    return render(request,'password_reset_done.html')

    
    #logout

def dealer_logout(request):
    logout(request)
    return redirect("dealer_login")
# ////////////////////


def index_main(request):
    items = Outlet.objects.all()
    return render(request, 'index_main.html',{'items':items} )


# views for add field..../


def outlet_add(request):
    if request.method == 'POST':
        # Extract data from the request
        item_name = request.POST.get('item-name')
        description = request.POST.get('description')
        start_time_str = request.POST.get('time-from')
        end_time_str = request.POST.get('time-to')
        item_img = request.FILES.get('image')

        # Basic validation (optional)
        if not item_name or not description or not start_time_str or not end_time_str:
            return render(request, 'add_fields.html', {'message': 'Please fill in all required fields'})

        # Try converting time strings to time objects
        try:
            start_time = datetime.strptime(start_time_str, '%H:%M').time()  # Parse time in HH:MM format
            end_time = datetime.strptime(end_time_str, '%H:%M').time()
        except ValueError:
            # Handle invalid time format
            return render(request, 'add_fields.html', {'message': 'Invalid time format. Use HH:MM format.'})

        # Create a new model object
        try:
            new_field = Outlet.objects.create(
                item_name=item_name, description=description, start_time=start_time, end_time=end_time, item_img=item_img)
            return redirect('outlet_add')  # Redirect to index_main after successful creation
        except Exception as e:  # Handle potential exceptions
            return render(request, 'add_fields.html', {'message': f'Error adding item: {str(e)}'})

    else:
        return render(request, 'add_fields.html', {'message': 'Invalid request method'})


## functions for outlet_deatails 
def outlet_deatails(request, pk):
    outlet_datas = get_object_or_404(OutletFields, pk=pk)
    # outlet_datas = OutletFields.objects.all()
    return render(request, 'outlet_deatails.html', {'items': outlet_datas})
 

## functions for outlet_adding

def outlet_fields_add(request):
    
    if request.method == 'POST':
        # Extract data from the request
        item_name = request.POST.get('item-name')
        description = request.POST.get('description')
        item_price = request.POST.get('item-price')
        about = request.POST.get('about')
        start_time_str = request.POST.get('time-from')
        end_time_str = request.POST.get('time-to')
        item_img = request.FILES.get('image')

        # Basic validation (optional)
        if not item_name or not description or not item_price or not about or not start_time_str or not end_time_str:
            return render(request, 'outlet_add.html', {'message': 'Please fill in all required fields'})

        # Try converting time strings to time objects
        try:
            start_time = datetime.strptime(start_time_str, '%H:%M').time()  # Parse time in HH:MM format
            end_time = datetime.strptime(end_time_str, '%H:%M').time()
        except ValueError:
            # Handle invalid time format
            return render(request, 'outlet_add.html', {'message': 'Invalid time format. Use HH:MM format.'})

        # Create a new model object
        try:
            new_field = OutletFields.objects.create(
                item_name=item_name, description=description,item_price=item_price,about=about, start_time=start_time, end_time=end_time, item_img=item_img)
            return redirect('index_main')  # Redirect to index_main after successful creation
        except Exception as e:  # Handle potential exceptions
            return render(request, 'outlet_add.html', {'message': f'Error adding item: {str(e)}'})

    else:
        return render(request, 'outlet_add.html')