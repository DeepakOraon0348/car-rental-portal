from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from myaddminpanel.models import *
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'index.html')

def search(request):
    cars = Car.objects.all()

    pickup_location = request.GET.get('pickup_location')
    car_type = request.GET.get('car_type')
    fuel_type = request.GET.get('fuel_type')
    transmission = request.GET.get('transmission')
    seats = request.GET.get('seats')
    min_price=request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if pickup_location:
        cars = cars.filter(
            pickup_location__icontains=pickup_location
        )

    if car_type:
        cars = cars.filter(
            car_name=car_type
        )

    if fuel_type:
        cars = cars.filter(
            fuel_type=fuel_type
        )

    if transmission:
        cars = cars.filter(
            transmission=transmission
        )
    if seats:
        cars = cars.filter(
            seats=seats
        )

    if max_price:
        cars = cars.filter(
            rent_per_day__lte=max_price
        )
    if max_price:
        cars = cars.filter(
            rent_per_day__gte=min_price
        )
      
    context = {
        'cars': cars
    }

    return render(request, 'search.html', context)

# def CarDetail(request):
#     return render(request, 'car-detail.html')

@csrf_exempt
def signup(request):
    print("tHIS VIEW IS RUNNING ")
    if request.method == 'POST':
        
        print("this method is working!")

        username = request.POST.get('fname')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')

        # Check passwords
        if password == confirm_password:

            # Create User
            my_user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
           
            my_user.save()

            print("User created successfully")

            return redirect('login')

        else:
            print("Password does not match")

            return redirect('')

    return render(request, 'signup.html')

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)

        user = authenticate(request, username=email, password=password)
        print(user)

        if user is not None:
            login(request, user)
            return redirect('search')
        else:
            print("Invalid credentials")
            return redirect('login')
    return render(request, 'login.html')
# ============================ logout view sectoin ======================
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')

    return redirect('profile')

@login_required
def profile(request):
    booking=Booking.objects.filter(user=request.user).select_related('car', 'vendor')
    booking_count=Booking.objects.filter(user=request.user).select_related('car').count();
     
    return render(request, 'profile.html', { 'booking':booking, 'booking_count':booking_count})
    
def akash(request):
    return render(request, 'akash.html')

# ======================== car details view.section =======================
def view_details(request, car_id):
    car = Car.objects.filter(id=car_id).first()  # Use .first() to get the actual object
    context = {
        'car': car
    }
    # data = model_to_dict(car)

    # data["image"] = car.image.url if car.image else None
    # print("Car details:", context)
    return render(request, 'view_detail.html', context)
    # return JsonResponse(data)
    
# ===============================car booking section =================================
def car_booking(request, car_id):
    # car = Car.objects.filter(id=car_id).first()  # Use .first() to get the actual object
    car = get_object_or_404(
        Car.objects.select_related(
            'driver',
            'vendor'
        ),
        id=car_id
    )
    context = {
        'car': car
    }
    print("Car:", car.car_name)
    print("Driver:", car.driver)
    
    return render(request, 'book.html', context)

# =======================accessing the booking details ==================
def booking_confirm(request, car_id):
    try:
        if request.method == "POST":

            car = Car.objects.get(id=car_id)

            Booking.objects.create(
                user=request.user,
                vendor=car.vendor,
                car=car,

                pickup_location=request.POST.get('pickup_location'),
                pickup_date=request.POST.get('pickup_date'),
                pickup_time=request.POST.get('pickup_time'),

                return_date=request.POST.get('return_date'),
                return_time=request.POST.get('return_time'),

                total_days=request.POST.get('total_days'),

                rent_per_day=car.rent_per_day,

            total_amount=request.POST.get('total_amount'),

                payment_method=request.POST.get('payment_method')
            )

            return redirect('car_booking')
    except Exception as e:
        return render(request, 'book.html', {'car':car})   