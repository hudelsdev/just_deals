from django.urls import path
from .views import *

urlpatterns =[
   path('deal_register',deal_register,name='deal_register'),  
   path('dealer_index',dealer_index,name='dealer_index'),  
   path('dealer_login',dealer_login,name='dealer_login'),  
   path('',index_main,name='index_main'),
   path('outlet_add',outlet_add,name='add_fields'), 
   path('outlet_deatails',outlet_deatails,name='outlet_deatails'),
   path('outlet_fields_add',outlet_fields_add,name='outlet_add'),
   path('unauthorized',unauthorized,name='unauthorized'),
  
]