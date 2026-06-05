from django.db import models

# Create your models here.

class vendorLogin(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=254, unique=True)
    phno= models.CharField(max_length=15)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
    # vendor=models.ForeignKey(vendorLogin,on_delete=models.CASCADE/SET_NULL,related_name='vendor')