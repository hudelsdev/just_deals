from django.urls import path
from .views import *

urlpatterns = [
    path('super_admin_login',super_admin_login,name='super_admin_login'),
    path('super_admin_logout',super_admin_logout,name='super_admin_logout'),


]