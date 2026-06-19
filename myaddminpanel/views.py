from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt


from myaddminpanel.models import *

# Create your views here.   
@csrf_exempt
def login_view(request):
    try:
       if request.method == 'POST':
           username = request.POST.get('username')
           password = request.POST.get('password')

           user = VendorLogin.objects.get(username=username, password=password)
           print(user)
           if user:
               request.session['vendor_id'] = user.id
               request.session['vendor_name'] = user.username
               VendorLogin (request, user)
               print("User logged in successfully")
               return redirect('vendor-profile')  # Replace 'home' with your actual home page URL name
    except VendorLogin.DoesNotExist:
        print("User does not exist")       
        return redirect('login_1')  # Replace 'login' with your actual login page URL name
    except VendorLogin.MultipleObjectsReturned:
        print("Duplicate Users Found")
    return render(request, 'login_1.html')

@csrf_exempt
def signup_1(request):
    if request.method == 'POST':
        
        username = request.POST.get('fname')
        email = request.POST.get('email')
        phno=request.POST.get('mobile')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')

        # Check passwords
        if password == confirm_password:

            # Create User
            my_user = VendorLogin.objects.create(
                username=username,
                email=email,
                phno=phno,
                password=password
            )
           
            my_user.save()

            print("User created successfully")

            return redirect('login_1')

        else:
            print("Password does not match")

            return redirect('signup-1')
    

def vendor_profile(request):
    vendor_id = request.session.get('vendor_id')

    print("Session Vendor ID:", vendor_id)

    if not vendor_id:
        return redirect('login_1')

    vendor = VendorLogin.objects.get(id=vendor_id)

    print("Current Vendor ID:", vendor.id)
    print("Current Vendor:", vendor)
    
    cars_count= Car.objects.filter(vendor=vendor).count()
    cars = Car.objects.filter(vendor=vendor)
    return render(request, 'vendorProfile.html' , {'vendor': vendor, 'cars': cars, 'cars_count': cars_count})

def logout_view_1(request):
    request.session.flush()
    print("User logged out successfully")
    return redirect('login_1')

def add_car(request):
    # Check if vendor is logged in
    vendor_id = request.session.get('vendor_id')

    if not vendor_id:
        return redirect('login_1')

    if request.method == 'POST':

        vendor = VendorLogin.objects.get(id=vendor_id)

        car = Car(
            vendor=vendor,

            car_name=request.POST.get('car_name'),
            brand=request.POST.get('brand'),
            model=request.POST.get('model'),
            year=request.POST.get('year'),

            city=request.POST.get('city'),
            pickup_location=request.POST.get('pickup_location'),

            rent_per_day=request.POST.get('rent_per_day'),

            fuel_type=request.POST.get('fuel_type'),
            transmission=request.POST.get('transmission'),

            seats=request.POST.get('seats') or 4,
            mileage=request.POST.get('mileage') or 0,

            ac='ac' in request.POST,
            power_steering='power_steering' in request.POST,
            power_windows='power_windows' in request.POST,
            music_system='music_system' in request.POST,
            airbags='airbags' in request.POST,
            gps='gps' in request.POST,

            status=request.POST.get('status'),

            description=request.POST.get('description'),

            image=request.FILES.get('image'),
            car_number=request.POST.get('car_number'),
            driver_name=request.POST.get('driver_name'),
            driver_license_number=request.POST.get('driver_license_number'),
            driver_license_expiry=request.POST.get('driver_license_expiry'),
            driver_age=request.POST.get('driver_age'),
            driver_ph_no=request.POST.get('driver_ph_no'),
            
        )

        car.save()

        print("Car Added Successfully")

        return redirect('vendor-profile')
    return render(request, 'addproduct.html')

# data fetching from database
# def view_cars(request):
#     print("VIEW CARS FUNCTION CALLED")
#     vendor_id = request.session.get('vendor_id')

#     print("Session Vendor ID:", vendor_id)

#     if not vendor_id:
#         return redirect('login_1')

#     vendor = VendorLogin.objects.get(id=vendor_id)

#     print("Current Vendor ID:", vendor.id)
#     print("Current Vendor:", vendor)

#     print("All Cars:", Car.objects.all())

#     cars = Car.objects.filter(vendor=vendor)

#     print("Cars Count:", cars.count())

#     return redirect('vendor-profile', {'cars': cars})

# ===================== fetching all cars to search bar =====================

