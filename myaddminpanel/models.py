from django.db import models

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

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.model}"