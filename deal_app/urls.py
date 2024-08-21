from django.urls import path
from .views import *

urlpatterns =[
   path('register_and_add_outlet',register_and_add_outlet,name='register_and_add_outlet'),  
   path('dealer_index',dealer_index,name='dealer_index'),  
   path('dealer_login',dealer_login,name='dealer_login'),  
   path('',index_main,name='index_main'),
   path('voucher_add',voucher_add,name='voucher_add'), 
   path('outlet_deatails/<int:pk>/',outlet_deatails,name='outlet_deatails'),
   # path('outlet_fields_add',outlet_fields_add,name='outlet_add'),
   path('unauthorized',unauthorized,name='unauthorized'),
   path('dealer_logout',dealer_logout,name='dealer_logout'),


]