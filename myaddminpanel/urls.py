from django.urls import include, path

from myapp.views import login_view
from .views import *

urlpatterns=[
     path('', login_view, name='login_1'),
]