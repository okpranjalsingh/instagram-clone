from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(max_length=30, blank=False, unique=True, null=False)
    email = models.EmailField(null=False, blank=False, unique=True)

class Follow(models.Model):
    follower = models.ForeignKey(
        "CustomUser",
        related_name="following_set",
        on_delete=models.CASCADE
    )
    following = models.ForeignKey(
        "CustomUser",
        related_name="followers_set",
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return f"{self.follower.username} → {self.following.username}"
