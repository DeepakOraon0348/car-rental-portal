from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

from myaddminpanel.models import VendorLogin

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
    
    return render(request, 'signup_1.html')

def vendor_profile(request):
    return render(request, 'vendorProfile.html')

def logout_view_1(request):
    request.session.flush()
    print("User logged out successfully")
    return redirect('login_1')