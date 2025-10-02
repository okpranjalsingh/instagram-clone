from django.db import models
from users.models import CustomUser

class Dm(models.Model):

    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="sent_dms")
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="received_dms")
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='dm_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"DM from {self.sender.username} to {self.receiver.username}"
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Direct Message"
        verbose_name_plural = "Direct Messages"

    username = models.CharField(max_length=30, blank=False, unique=True, null=False)
    textings = models.TextField(blank=False, null=False)
    image = models.ImageField(blank=True, null=True)
    sender = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return self.username, self.sender

class Info(models.Model):
    def __init__(self, sender, reciver, updated_at):
        self.sender = sender
        self.reviver = reciver
        self.updated_at = updated_at
        pass

    
