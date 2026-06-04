from django.urls import include, path

from myapp.views import login_view, signup
from .views import *

urlpatterns=[
     path('', login_view, name='login_1'),
     path('signup_1/', signup_1, name='signup-1'),
    #  path('add-car/', add_car, name='add-car'),
    path('vendor-profile/', vendor_profile, name='vendor-profile'),
]