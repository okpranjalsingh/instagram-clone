from django.db import models
from users.models import CustomUser

# Create your models here.

class Dm(models.Model):
    username = models.CharField(max_length=30, blank=False, unique=True, null=False)
    textings = models.TextField(blank=False, null=False)
    image = models.ImageField(blank=True, null=True)



    
    
    

