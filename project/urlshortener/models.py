from django.db import models
from .utils import create_shortened_url
from django.contrib.auth.models import User, update_last_login
from django.db.models.deletion import CASCADE

class Shortener(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    times_followed = models.PositiveIntegerField(default=0)
    long_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True, blank=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f'{self.long_url} to {self.short_url}'


    def save(self, *args, **kwargs):


        if not self.short_url:

            self.short_url = create_shortened_url(self)

        super().save(*args, **kwargs)


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to ='profile_pics')