from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    dob = models.DateField(null=True, blank=True)

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)

    bio = models.CharField(max_length=150, null=True, blank=True)
    profile_pic = models.ImageField(
        upload_to="profile_pics/", 
        null=True,
        blank=True,
        default='profile_pics/default.jpg'
    )

    def __str__(self):
        return f"{self.user.username}'s profile"