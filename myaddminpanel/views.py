from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

from myaddminpanel.models import vendorLogin

# Create your views here.
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = vendorLogin.objects.get(username=username, password=password)
        print(user)
        if user:
            vendorLogin(request, user)
            return redirect('vendor-profile')  # Replace 'home' with your actual home page URL name
        else:
            print("Invalid credentials")
            return redirect('login_1')  # Replace 'login' with your actual login page URL name
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
            my_user = vendorLogin.objects.create(
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
    
    return render(request, 'signup_1.html')

def vendor_profile(request):
    return render(request, 'vendorProfile.html')

def logout_view_1(request):
    logout(request)
    return redirect('login_1')