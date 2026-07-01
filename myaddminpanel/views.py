from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from myaddminpanel.models import *


# Create your views here.
@csrf_exempt
def login_view(request):
    try:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = VendorLogin.objects.get(username=username, password=password)
            if user:
                request.session["vendor_id"] = user.id
                request.session["vendor_name"] = user.username
                VendorLogin(request, user)
                print("User logged in successfully")
                return redirect(
                    "vendor-profile"
                )  # Replace 'home' with your actual home page URL name
    except VendorLogin.DoesNotExist:
        print("User does not exist")
        return redirect(
            "login_1"
        )  # Replace 'login' with your actual login page URL name
    except VendorLogin.MultipleObjectsReturned:
        print("Duplicate Users Found")
    return render(request, "login_1.html")


@csrf_exempt
def signup_1(request):
    if request.method == "POST":

        username = request.POST.get("fname")
        email = request.POST.get("email")
        phno = request.POST.get("mobile")
        password = request.POST.get("password1")
        confirm_password = request.POST.get("password2")

        # Check passwords
        if password == confirm_password:

            # Create User
            my_user = VendorLogin.objects.create(
                username=username, email=email, phno=phno, password=password
            )

            my_user.save()

            print("User created successfully")

            return redirect("login_1")

        else:
            print("Password does not match")

            return redirect("signup-1")


def vendor_profile(request):
    vendor_id = request.session.get("vendor_id")

    print("Session Vendor ID:", vendor_id)

    if not vendor_id:
        return redirect("login_1")

    vendor = VendorLogin.objects.get(id=vendor_id)

    print("Current Vendor ID:", vendor.id)
    print("Current Vendor:", vendor)

    cars_count = Car.objects.filter(vendor=vendor).count()
    cars = Car.objects.filter(vendor=vendor)
    return render(
        request,
        "vendorProfile.html",
        {"vendor": vendor, "cars": cars, "cars_count": cars_count},
    )


def logout_view_1(request):
    request.session.flush()
    print("User logged out successfully")
    return redirect("login_1")


def add_car(request):
    # Check if vendor is logged in
    vendor_id = request.session.get("vendor_id")

    if not vendor_id:
        return redirect("login_1")

    vendor = VendorLogin.objects.get(id=vendor_id)

    drivers = Driver.objects.filter(vendor_id=vendor_id)
    print(drivers)
    if request.method == "POST":

        driver_id = request.POST.get("driver")
        driver = None

        if driver_id:
            driver = Driver.objects.get(id=driver_id)

        car = Car(
            vendor=vendor,
            driver=driver,
            car_name=request.POST.get("car_name"),
            brand=request.POST.get("brand"),
            model=request.POST.get("model"),
            year=request.POST.get("year"),
            city=request.POST.get("city"),
            pickup_location=request.POST.get("pickup_location"),
            rent_per_day=request.POST.get("rent_per_day"),
            fuel_type=request.POST.get("fuel_type"),
            transmission=request.POST.get("transmission"),
            seats=request.POST.get("seats") or 4,
            mileage=request.POST.get("mileage") or 0,
            ac="ac" in request.POST,
            power_steering="power_steering" in request.POST,
            power_windows="power_windows" in request.POST,
            music_system="music_system" in request.POST,
            airbags="airbags" in request.POST,
            gps="gps" in request.POST,
            status=request.POST.get("status"),
            description=request.POST.get("description"),
            image=request.FILES.get("image"),
        )

        car.save()

        print("Car Added Successfully")

        return redirect("vendor-profile")
    return render(request, "addproduct.html", {"drivers": drivers})


def add_driver(request):
    vendor_id = request.session.get("vendor_id")

    if not vendor_id:
        return redirect("login_1")

    vendor = VendorLogin.objects.get(id=vendor_id)

    if request.method == "POST":
        Driver.objects.create(
            vendor=vendor,
            driver_name=request.POST.get("driver_name"),
            driver_license_number=request.POST.get("driver_license_number"),
            driver_license_expiry=request.POST.get("driver_license_expiry"),
            driver_age=request.POST.get("driver_age"),
            driver_ph_no=request.POST.get("driver_ph_no"),
        )

        return redirect("add-car")

    return render(request, "driverInfo.html")


def book_history(request):
    print("hey i am working!")
    try:
        vendor_id = request.session.get("vendor_id")
        bookings = Booking.objects.filter(vendor_id=vendor_id)
        context = {"bookings": bookings}
        print(context)
        return render(request, "booking_history.html", context)
    except Exception as e:
        return redirect("vendor-profile")
    return render(request, "booking_history.html")


def accept_booking(request, book_id):
    book = get_object_or_404(Booking.objects.filter(id=book_id))
    book.status = "Confirmed"
    book.save()

    return redirect("book_history")


def reject_booking(request, book_id):
    book = get_object_or_404(Booking.objects.filter(id=book_id))
    book.status = "Rejected"
    book.save()

    return redirect("book_history")


def updateDriver(request, car_id):
    cars = get_object_or_404(
        Car.objects.filter(id=car_id).select_related("driver", "vendor")
    )
    driver = cars.driver

    if request.method == "POST":
        driver.driver_name = request.POST.get("driver_name")
        driver.driver_ph_no = request.POST.get("driver_ph_no")
        driver.driver_license_number = request.POST.get("driver_license_number")
        driver.driver_license_expiry = request.POST.get("driver_license_expiry")
        driver.driver_age = request.POST.get("driver_age")

        driver.save()

        return redirect("updateCar", car_id=cars.id)
    context = {"car": cars}

    return render(request, "updateDrivers.html", context)


def updateCar(request, car_id):
    car = get_object_or_404(Car.objects.select_related("vendor"), id=car_id)

    vendor = car.vendor
    try:
        drivers = Driver.objects.filter(vendor=vendor)
    except:
        print("Driver does not Exist!")
        
    if request.method == "POST":

        car.car_name = request.POST.get("car_name")
        car.brand = request.POST.get("brand")
        car.model = request.POST.get("model")
        car.year = request.POST.get("year")
        car.city = request.POST.get("city")
        car.pickup_location = request.POST.get("pickup_location")
        car.rent_per_day = request.POST.get("rent_per_day")
        car.fuel_type = request.POST.get("fuel_type")
        car.transmission = request.POST.get("transmission")

        driver_id = request.POST.get("driver")
        if driver_id:
            car.driver = Driver.objects.get(id=driver_id)

        car.seats = request.POST.get("seats")
        car.mileage = request.POST.get("mileage")

        car.ac = "ac" in request.POST
        car.power_steering = "power_steering" in request.POST
        car.power_windows = "power_windows" in request.POST
        car.music_system = "music_system" in request.POST
        car.airbags = "airbags" in request.POST
        car.gps = "gps" in request.POST

        image = request.FILES.get("image")
        if image:
            car.image = image

        car.status = request.POST.get("status")
        car.description = request.POST.get("description")

        car.save()

        return redirect("vendor-profile")

    return render(request, "update.html", {"car": car, "drivers": drivers})
