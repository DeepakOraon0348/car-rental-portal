from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from myaddminpanel.models import *


# Create your views here.
def index(request):
    return render(request, 'index.html')

def search(request):
    cars = Car.objects.all()
    print(cars)
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

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')

    return redirect('profile')


def profile(request):
    return render(request, 'profile.html')
def akash(request):
    return render(request, 'akash.html')

def view_details(request, car_id):
    car = Car.objects.filter(id=car_id).first()  # Use .first() to get the actual object
    context = {
        'car': car
    }
    print("Car details:", context)
    return render(request, 'view_detail.html', context)
def car_booking(request, car_id):
    return render(request, 'book.html')