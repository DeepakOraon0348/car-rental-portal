from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class VendorLogin(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=254, unique=True)
    phno= models.CharField(max_length=15)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
    # vendor=models.ForeignKey(VendorLogin,on_delete=models.CASCADE/SET_NULL,related_name='vendor')

class Driver(models.Model):
    vendor = models.ForeignKey(
        VendorLogin,
        on_delete=models.CASCADE,
        related_name='drivers'
    )
    driver_name = models.CharField(max_length=225)
    driver_license_number = models.CharField(max_length=50)
    driver_license_expiry = models.DateField()
    driver_age = models.PositiveIntegerField()
    driver_ph_no = models.CharField(max_length=15)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.driver_name
    
    
class Car(models.Model):

    TRANSMISSION_CHOICES = [
        ('Manual', 'Manual'),
        ('Automatic', 'Automatic'),
    ]

    FUEL_CHOICES = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('CNG', 'CNG'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
    ]

    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Booked', 'Booked'),
        ('Maintenance', 'Maintenance'),
    ]

    vendor = models.ForeignKey(
        VendorLogin,
        on_delete=models.CASCADE,
        related_name='cars'
    )

    # Basic Details
    car_name = models.CharField(max_length=100, blank=True, null=True)
    brand = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    year = models.PositiveIntegerField(blank=True, null=True)

    # Location
    city = models.CharField(max_length=100, blank=True, null=True)
    pickup_location = models.CharField(max_length=200, blank=True, null=True)

    # Pricing
    rent_per_day = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    # Vehicle Details
    fuel_type = models.CharField(
        max_length=20,
        choices=FUEL_CHOICES
    )

    transmission = models.CharField(
        max_length=20,
        choices=TRANSMISSION_CHOICES
    )

    seats = models.PositiveIntegerField(default=4)

    mileage = models.PositiveIntegerField(default=0)

    # Features
    ac = models.BooleanField(default=True)
    power_steering = models.BooleanField(default=True)
    power_windows = models.BooleanField(default=True)
    music_system = models.BooleanField(default=False)
    airbags = models.BooleanField(default=True)
    gps = models.BooleanField(default=False)

    # Images
    image = models.ImageField(
        upload_to='cars/',
        blank=True,
        null=True
    )

    # Status
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Available'
    )

    description = models.TextField(
        blank=True,
        null=True
    )
    driver = models.ForeignKey(
        Driver,
        on_delete=models.SET_NULL,
        null=True, 
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.model}"
    
    
class Booking(models.Model):
    STATUS_CHOICES=[
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Rejected', 'Rejected'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
       
    PAYMENT_METHOD_CHOICES=[
        ('Pay Now', 'Pay Now'),
        ('Pay at Pickup', 'Pay at Pickup'),
    ] 
    
    PAYMENT_STATUS_CHOICES=[
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
        ('Failed', 'Failed'),
        ('Refunded', 'Refunded'),
    ]
    user= models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='bookings'
    )
        
    vendor = models.ForeignKey(
        VendorLogin,
        on_delete=models.CASCADE,
        related_name='bookings'
    )
        
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name='booking'
    )
    pickup_location=models.CharField(max_length=200)
    # dropup_location=models.CharField(max_length=200)
    
    pickup_date=models.DateField()
    pickup_time=models.TimeField()
    return_date=models.DateField()
    return_time=models.TimeField()
    total_days=models.PositiveIntegerField()
    rent_per_day=models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    
    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHOD_CHOICES
    )
    
    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS_CHOICES,
        default='Pending'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )
    booked_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Booking #{self.id}-{self.car.car_name}"
    
    