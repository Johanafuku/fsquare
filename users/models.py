
from django.db import models
from django.contrib.auth.models import User

class Designer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to="profile_pictures/",blank=True,null=True)
    bio = models.TextField(max_length=500, blank=True)
    email = models.EmailField(max_length=100,blank=True)
    

    def __str__(self):
        return self.brand_name
