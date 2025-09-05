from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from profiles.models import Profile

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        print(">>> Signal Triggered: Creating profile for", instance.username)
        Profile.objects.create(user=instance)
    else:
        print(">>> Signal Triggered: Updating profile for", instance.username)
        if hasattr(instance, "profile"):
            instance.profile.save()
