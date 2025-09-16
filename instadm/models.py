from django.db import models

# Create your models here.

class Dm(models.Model):
    username = models.ForeignKey(on_delete=models.CASCADE)
    textings = models.TextField(blank=False, null=False)
    image = models.ImageField(blank=True, null=True)


  def save(self, *args, **kwargs):
        if self.pk:
            [Count number of users following self]
            [Set self.number_of_followers to counted number]
        super(Feed, self).save(*args, **kwargs)