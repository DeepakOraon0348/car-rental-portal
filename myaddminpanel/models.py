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

# class Car(models.Model):
#     vendor = models.ForeignKey(VendorLogin, on_delete=models.CASCADE, related_name='cars')
#     car_name = models.CharField(max_length=100, blank=True, null=True)
#     car_model = models.CharField(max_length=100, blank=True, null=True)
#     car_year = models.PositiveIntegerField(max_length=4, blank=True, null=True)
#     price_per_day = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
#     availability_status = models.BooleanField(default=True)

#     def __str__(self):
#         return f"{self.car_name}" if self.car_name else f"{self.car_model} ({self.car_year})"