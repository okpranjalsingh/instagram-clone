from django.db import models

# Create your models here.

class Dm(models.Model):
    username = models.CharField(max_length=30, blank=False, unique=True, null=False)
    textings = models.TextField(blank=False, null=False)
    image = models.ImageField(blank=True, null=True)


    def __str__(self):
        return self.username
    
    
    

