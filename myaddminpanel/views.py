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
        print(username, password)

        user = authenticate(request, username=username  , password=password)
        if user:
            login(request, user)
            return redirect('vendor-profile')  # Replace 'home' with your actual home page URL name
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