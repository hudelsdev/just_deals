from django.urls import path
from .views import *
from deal_app.views import*

urlpatterns = [
    path('super_admin_login',super_admin_login,name='super_admin_login'),
    path('super_admin_logout',super_admin_logout,name='super_admin_logout'),
    path('outlet_list',outlet_list,name='outlet_list'),
    path('outlet_items_edit/<int:pk>/',outlet_items_edit,name='outlet_items_edit'),
    path('outlet_items_delete/<int:pk>/',outlet_items_delete,name='outlet_items_delete'),

    

]