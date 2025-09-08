from django.db import models
from django.conf import settings 

class Post(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    image = models.ImageField(upload_to='post-images/')  
    caption = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

    class Meta:
        ordering = ['-created_at'] 

    def __str__(self):
        return f"{self.user.username}'s post at {self.created_at}"
