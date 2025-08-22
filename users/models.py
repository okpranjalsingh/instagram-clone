from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    email = models.EmailField(null=False, unique=True)
    bio = models.CharField(max_length=100, null= True, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'username']

    def __str__(self):
        return self.email
    
    