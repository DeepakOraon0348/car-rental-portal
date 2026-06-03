from django.urls import include, path
from .views import *

urlpatterns=[
    path('', index, name='index'),
    path('/search',search, name='search'),
    path('car-detail/', CarDetail, name='car-detail'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('/profile', profile , name='profile'),
    path('/akash', akash, name='akash')
]