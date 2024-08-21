from django.urls import path
from .views import *
from deal_app.views import*

urlpatterns = [
    path('super_admin_login',super_admin_login,name='super_admin_login'),
    path('super_admin_logout',super_admin_logout,name='super_admin_logout'),
    path('dealer_vouchers',dealer_vouchers,name='dealer_vouchers'),
    path('outlet_items_edit/<int:pk>/',voucher_items_edit,name='outlet_items_edit'),
    path('outlet_items_delete/<int:pk>/',voucher_items_delete,name='outlet_items_delete'),
]