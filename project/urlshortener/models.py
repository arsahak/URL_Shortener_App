from django.db import models
from .utils import create_shortened_url
from datetime import datetime, date

class Shortener(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    times_followed = models.PositiveIntegerField(default=0)
    expired_date = models.DateTimeField(auto_now_add=False, null=True)
    long_url = models.URLField()
    custom_url = models.URLField(max_length=15, unique=True, null=True)
    short_url = models.CharField(max_length=15, unique=True, blank=True)

    class Meta:
        ordering = ["-created"]
    def __str__(self):
        return f'{self.expired_date},{self.long_url},{self.custom_url},{self.short_url}'


    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = create_shortened_url(self)
        super().save(*args, **kwargs)

class OneToOneField:
    pass