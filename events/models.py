from django.db import models
from datetime import datetime

# Create your models here.


class Events(models.Model):
    event_name = models.CharField(max_length=200)
    description = models.TextField()
    ticket_url = models.URLField()
    image = models.ImageField(upload_to='events/')
    event_date = models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(default=datetime.now)
    active = models.BooleanField()

    def __str__(self):
        return self.event_name

    class Meta:
        verbose_name_plural = 'Events'
