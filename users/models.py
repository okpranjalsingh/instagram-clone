from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(max_length=30, blank=False, unique=True, null=False)
    email = models.EmailField(null=False, blank=False, unique=True)


    def __str__(self):
        return self.username