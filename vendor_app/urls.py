from django.urls import path
from .views import *

urlpatterns =[
   path('vendor_register',vendor_register,name='vendor_register'),  
   


]