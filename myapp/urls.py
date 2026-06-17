from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from CarRentalPortal import settings
from .views import *

urlpatterns=[
    path('', index, name='index'),
    path('/search',search, name='search'),
    # path('car-detail/', CarDetail, name='car-detail'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('/profile', profile , name='profile'),
    path('/akash', akash, name='akash'),
    path('logout/', logout_view, name='logout'),
    path('view_details/<int:car_id>/', view_details, name='view_details'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )