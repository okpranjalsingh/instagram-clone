from django.db import models

# Create your models here.

class Dm(models.Model):
    username = models.ForeignKey(on_delete=models.CASCADE)
    textings = models.TextField(blank=False, null=False)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.username
    
    

    

